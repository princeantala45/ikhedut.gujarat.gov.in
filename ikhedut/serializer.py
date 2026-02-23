from ikhedut.models import Ad, CropSale,Contact,Order, Signup
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class Cropsaleserializers(serializers.ModelSerializer):
    class Meta:
        model = CropSale
        exclude = ["seller", "is_approved"]
        
    def validate(self, data):
        # crop must be select fron list in frontend selection
        if not data.get("crop"):
            raise serializers.ValidationError({
                "crop": "Crop is required"
            })
        # crop not take numeric value
        if data.get("crop").isnumeric():
            raise serializers.ValidationError({
                "crop": "Crop must not be numeric"
            })        
        
        return data

class Conactserializers(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'
        
    def validate(self, data):
        # mobile must be 10 digit or not take alphabet value        
        if len(data.get("mobile")) != 10:
            raise serializers.ValidationError({
                "mobile": "Mobile number must be 10 digits"
            })
        # mobile not take alphabet value
        if not data.get("mobile").isnumeric():
            raise serializers.ValidationError({
                "mobile": "Mobile number must be numeric"
            })
                        
        return data
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "fullname",
            "mobile",
            "city",
            "pincode",
            "address",
            "payment_method",
            "cardholdername",
            "card_number",
            "card_expiry",
            "card_cvv",
            "upi_id",
        ]

    def validate(self, data):
        # mobile fix 10 digit 
        if len(data.get("mobile")) != 10:
            raise serializers.ValidationError({
                "mobile": "Mobile number must be 10 digits"
            })
        # pincode 6 digit only 
        if len(data.get("pincode")) != 6:
            raise serializers.ValidationError({
                "pincode": "Pincode must be 6 digits"
            })
    
        payment_method = data.get("payment_method")

        if payment_method == "CARD":
            required = ["cardholdername", "card_number", "card_expiry", "card_cvv"]
            for field in required:
                if not data.get(field):
                    raise serializers.ValidationError({
                        field: "This field is required for card payment"
                    })
        # cardnumber take fix 16 digit 
        if payment_method == "CARD" and len(data.get("card_number")) != 16:
            raise serializers.ValidationError({
                "card_number": "Card number must be 16 digits"
            })
        # card expiry 
        if payment_method == "CARD" and len(data.get("card_expiry")) != 5:
            raise serializers.ValidationError({
                "card_expiry": "Card expiry must be 5 digits"
            })

        # card cvv 
        if payment_method == "CARD" and len(data.get("card_cvv")) != 3:
            raise serializers.ValidationError({
                "card_cvv": "Card CVV must be 3 digits"
            })

        if payment_method == "UPI" and not data.get("upi_id"):
            raise serializers.ValidationError({
                "upi_id": "UPI ID is required for UPI payment"
            })

        return data
       
class PostAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [
            "id",
            "fullname",
            "mobile",
            "state",
            "city",
            "productname",
            "description",
            "price",
            "image",
            "is_approved",
        ]
        read_only_fields = ["is_approved"]
        
        def validate(self,data):
            
            if not data["mobile"].isnumeric():
                raise serializers.ValidationError({
                    "mobile": "Mobile number must be numeric"
                })
            if len(data["mobile"]) != 10:
                raise serializers.ValidationError({
                    "mobile": "Mobile number must be 10 digits"
                })
            return data 
        
class UserSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    repassword = serializers.CharField(write_only=True, required=True)
    mobile = serializers.CharField(write_only=True, required=True)
    image = serializers.ImageField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "repassword", "mobile", "image"]

    def validate(self, data):
        if data["password"] != data["repassword"]:
            raise serializers.ValidationError({
                "password": "Passwords do not match"
            })

        if User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError({
                "username": "Username already exists"
            })

        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError({
                "email": "Email already exists"
            })
        
        if len(data["password"]) < 8:
            raise serializers.ValidationError({
                "password": "Password must be at least 8 characters long"
            })
        
        if not any(char.isdigit() for char in data["password"]):
            raise serializers.ValidationError({
                "password": "Password must contain at least one number"
            })
        
        if not any(char.isupper() for char in data["password"]):
            raise serializers.ValidationError({
                "password": "Password must contain at least one uppercase letter"
            })
        
        if not any(char.islower() for char in data["password"]):
            raise serializers.ValidationError({
                "password": "Password must contain at least one lowercase letter"
            })
            
        if not any(char.isalnum() for char in data["password"]):
            raise serializers.ValidationError({
                "password": "Password must contain at least one special character"
            })
        
        if len(data["mobile"]) != 10:
            raise serializers.ValidationError({
                "mobile": "Mobile number must be 10 digits"
            })

        return data

    def create(self, validated_data):
        validated_data.pop("repassword")
        mobile = validated_data.pop("mobile")
        image = validated_data.pop("image")
        password = validated_data.pop("password")

        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(password)
        user.save()

        Signup.objects.create(
            user=user,
            mobile=mobile,
            image=image
        )

        return user

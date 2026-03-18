from django.db import models


class SprayPump(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=100)  # Eco-Friendly / Best Seller / Heavy Duty
    tagline_color = models.CharField(max_length=50)  # green-500 / blue-500 / red-500
    operation_type = models.CharField(max_length=100)  # Hand Operated / Rechargeable
    operation_color = models.CharField(max_length=50)  # text-green-600 etc
    description = models.TextField()

    feature_1 = models.CharField(max_length=200)
    feature_2 = models.CharField(max_length=200)
    feature_3 = models.CharField(max_length=200)

    image = models.ImageField(upload_to="spray-pump/")
    order = models.PositiveIntegerField(default=0)

    # Technical specs
    pressure = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

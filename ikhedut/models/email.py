from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime

class OTPRequest(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        # OTP is valid for 5 minutes
        return timezone.now() < self.created_at + datetime.timedelta(minutes=5)
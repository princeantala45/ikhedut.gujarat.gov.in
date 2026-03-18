from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="signup"
    )
    mobile = models.CharField(max_length=60)
    image = models.ImageField(upload_to="userimages/", blank=True, null=True)

    def __str__(self):
        return self.user.username

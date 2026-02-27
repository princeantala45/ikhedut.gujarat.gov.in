from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ads",
        null=True,
        blank=True
    )
    fullname = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50)
    state = models.CharField(max_length=50, default="Gujarat")
    city = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="ad_img/", null=True, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        if self.user:
            return f"{self.productname} ({self.user.username})"
        return self.productname

    def save(self, *args, **kwargs):
        if self.productname:
            self.productname = self.productname.title()
        super().save(*args, **kwargs)
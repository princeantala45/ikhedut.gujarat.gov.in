from django.db import models
from django.contrib.auth.models import User

class CropSale(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    crop = models.CharField(max_length=50, db_index=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="crop_img/", null=True, blank=True)
    is_approved = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.crop

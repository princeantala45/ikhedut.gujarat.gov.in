from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

from .cropsale import CropSale

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=30)

class Cartitems(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,   
        related_name="items"
    )
    product = models.ForeignKey(
        CropSale,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField(default=20)
    added_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.added_at + timedelta(minutes=30)

    @property
    def subtotal(self):
        if not self.product:
            return 0
        return round((self.product.price / 20) * self.quantity, 2)
    
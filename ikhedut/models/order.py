from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

from .cropsale import CropSale

class Order(models.Model):
    STATUS_CHOICES = (
        ("placed", "Placed"),
        ("cancel_requested", "Cancel Requested"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
        null=True,
        blank=True
    )

    fullname = models.CharField(max_length=150)
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    address = models.TextField()

    payment_method = models.CharField(max_length=20)

    cardholdername = models.CharField(max_length=50, blank=True, null=True)
    card_number = models.CharField(max_length=25, blank=True, null=True)
    card_expiry = models.CharField(max_length=10, blank=True, null=True)
    card_cvv = models.CharField(max_length=10, blank=True, null=True)
    upi_id = models.CharField(max_length=100, blank=True, null=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="placed"
    )

    cancel_requested_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def can_cancel(self):
        return (
            self.status == "placed"
            and timezone.now() <= self.created_at + timedelta(hours=24)
        )

    def should_be_completed(self):
        return (
            self.status == "placed"
            and timezone.now() >= self.created_at + timedelta(days=10)
        )

    def __str__(self):
        return f"Order #{self.fullname}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    product = models.ForeignKey(
        CropSale,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order.id} Item" # type: ignore

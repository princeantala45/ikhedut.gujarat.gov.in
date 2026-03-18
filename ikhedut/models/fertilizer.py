from django.db import models

class Fertilizer(models.Model):
    name = models.CharField(max_length=200)
    nutrient = models.CharField(max_length=200)
    best_for = models.CharField(max_length=200)
    benefits = models.CharField(max_length=200)
    weight = models.CharField(max_length=50)
    price_range = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Fertilizer/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

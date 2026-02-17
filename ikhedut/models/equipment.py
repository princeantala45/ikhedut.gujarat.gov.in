from django.db import models

class Equipment(models.Model):
    CATEGORY_CHOICES = [
        ("Primary Tillage", "Primary Tillage"),
        ("Secondary Tillage", "Secondary Tillage"),
        ("Primary / Secondary", "Primary / Secondary"),
        ("Seedbed Preparation", "Seedbed Preparation"),
        ("Deep Tillage", "Deep Tillage"),
        ("Transport", "Transport"),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Tillage_equipment/")
    order = models.PositiveIntegerField(
    default=0,
    blank=False,
    null=False,
    db_index=True
)


    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.name

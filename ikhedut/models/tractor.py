from django.db import models

class Tractor_Page(models.Model):
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    image = models.ImageField(upload_to="Teactor_page_image/")
    tractor_name = models.CharField(max_length=50)
    Engine = models.CharField(max_length=200)
    Transmission = models.CharField(max_length=200)
    Hydraulics = models.CharField(max_length=200)
    Brake = models.CharField(max_length=200)
    Steering = models.CharField(max_length=200)
    FuelTank = models.CharField(max_length=200)
    Tyres = models.CharField(max_length=200)
    Build = models.CharField(max_length=200)
    Price = models.CharField(max_length=200)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.tractor_name

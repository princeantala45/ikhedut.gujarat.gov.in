from django.db import models

class Ox(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    description = models.TextField()
    feauter_1=models.CharField(max_length=200)
    feauter_2=models.CharField(max_length=200)
    feauter_3=models.CharField(max_length=200)
    feauter_4=models.CharField(max_length=200)
    weight_range = models.CharField(max_length=100)
    image = models.ImageField(upload_to="ox_page/")
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

from django.db import models

class AgroChemical(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=100)
    pack_size = models.CharField(max_length=100)
    use = models.CharField(max_length=100)
    price = models.CharField(max_length=200)
    image = models.ImageField(upload_to="agrochemicals/")
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

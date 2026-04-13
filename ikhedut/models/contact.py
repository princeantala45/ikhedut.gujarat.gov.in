from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    mobile = models.CharField(max_length=60)
    message = models.TextField()

    def __str__(self):
        return self.name

from django.db import models
class AgricultureGuidance(models.Model):
    image=models.ImageField(upload_to="Agriculture_guidance/")
    crop_name=models.CharField(max_length=300)
    crop_season=models.CharField(max_length=300)
    crop_Sowing=models.CharField(max_length=300)
    crop_Harvest=models.CharField(max_length=200)   
    crop_Soil=models.CharField(max_length=300)
    crop_Water=models.CharField(max_length=300)
    crop_Seed_rate=models.CharField(max_length=300)
    crop_Fertilizer=models.CharField(max_length=300)
    crop_Problems=models.CharField(max_length=300)
    crop_Yield=models.CharField(max_length=300)
    order=models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
    
    def __str__(self):
        return self.crop_name
    
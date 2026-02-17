
from django.db import models

class Slider(models.Model):
    image=models.ImageField(upload_to="main-slider-image/")
    is_active = models.BooleanField(default=False)
    
class Slider2(models.Model):
    image=models.ImageField(upload_to="second-slider-image/")
    is_active=models.BooleanField(default=False)

class Slider_content(models.Model):
    first_line_text=models.TextField(max_length=500,blank=False)
    second_line_text=models.TextField(max_length=500,blank=False)

    def __str__(self):
        return "Content of Slider"
    
class Navbar(models.Model):
    page_name = models.CharField(max_length=100)
    page_url = models.CharField("Page URL", max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.page_name 
    

class SupportedCompany(models.Model):
    company_image=models.ImageField(upload_to="Supported-company-image/")
    is_active=models.BooleanField(default=False)
    company_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["company_order"]
        

class QuickLink(models.Model):
    q_page_name = models.CharField(max_length=100)
    q_page_url = models.CharField(max_length=200)
    q_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["q_order"]

    def __str__(self):
        return self.q_page_name
class Informations(models.Model):
    info_image = models.ImageField(upload_to="Information_image/")
    info_title = models.CharField(max_length=50)
    info_text = models.CharField(max_length=250)  
    info_button_url = models.CharField(max_length=50)
    position = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return self.info_title
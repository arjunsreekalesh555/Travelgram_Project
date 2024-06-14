from django.db import models

# Create your models here.
class Travelgram(models.Model):
    Place_name=models.CharField(max_length=250)
    Weather=models.CharField(max_length=250)
    Location=models.CharField(max_length=250)
    Map=models.URLField(max_length=500)
    Place_img=models.ImageField(upload_to='places/')
    Description=models.TextField(max_length=5000)
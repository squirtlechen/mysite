from django.db import models
from django.urls import reverse

# Create your models here.
class Table(models.Model):
    title    = models.CharField(default="",max_length = 60)
    

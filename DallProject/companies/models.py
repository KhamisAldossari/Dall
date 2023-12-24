from django.db import models

#Create your models here.
class Copmany(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    industry=models.CharField(max_length=100)
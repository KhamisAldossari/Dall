from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    jops= models.ManyToManyField(Jop)


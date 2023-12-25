from django.db import models

# Create your models here.
class Certificate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    provider= models.CharField(max_length=100)
    certificate_image=models.ImageField(upload_to="images/", default="images/avatar-default.png")

    def __str__(self):
        return self.name
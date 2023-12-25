from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration= models.CharField(max_length=100)
    provider= models.CharField(max_length=100)
    course_image=models.ImageField(upload_to="images/", default="images/avatar-default.png")
    

    def __str__(self):
        return self.name
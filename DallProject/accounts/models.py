from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    birth_date = models.DateField()
    profile_picture = models.ImageField(upload_to="images/", default="images/avatar-default.png")
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=100, blank= True, null=True)
    degree = models.CharField(max_length=100, blank= True, null=True)
    university_name = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"{self.user.first_name} Profile"
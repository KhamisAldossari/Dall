from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    post_user=models.ForeignKey(User, on_delete=models.CASCADE)
    post_image=models.ImageField(upload_to="images/", default="images/avatar-default.png")
    video = models.FileField(upload_to='video/',null=True)
    def __str__(self):
        return self.title
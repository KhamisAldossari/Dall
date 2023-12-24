from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
# Create your models here.
class Reply(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField() 
    date_posted=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    reply_user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
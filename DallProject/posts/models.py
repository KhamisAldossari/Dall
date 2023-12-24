from django.db import models
from replies.models import Reply
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    replies=models.ForeignKey(Reply,on_delete=models.CASCADE)
from django.db import models
from django.contrib.auth.models import User
from majors.models import Major

# Create your models here.
class Favorite(models.Model):
    major=models.ForeignKey(Major, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):

        return f"{self.user.username} favored {self.major.name}"
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __int__(self):
        return f"{self.title}"
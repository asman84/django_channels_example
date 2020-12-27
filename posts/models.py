from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    text_size = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

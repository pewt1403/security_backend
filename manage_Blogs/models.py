from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=2100)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)


class Comment(models.Model):
    Blogs = models.ForeignKey(Blog, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=700)
    score = models.IntegerField(default=0)
    edited = models.BooleanField(default=False)

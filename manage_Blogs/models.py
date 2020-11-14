import datetime

from django.utils import timezone
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=30)
    content = models.CharField(max_length=2100)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.title)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    @classmethod
    def create(cls, title, content):
        blog = cls(title=title, content=content, score=0, pub_date= timezone.now())
        return blog

class Comment(models.Model):
    Blogs = models.ForeignKey(Blog, on_delete=models.CASCADE)
    creator = models.CharField(max_length=30)
    pub_date =  models.DateTimeField('date published')
    comment = models.CharField(max_length=700)
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.comment)

    @classmethod
    def create(cls, comment, blogId):
        newComment = cls(creator='', score=0, pub_date=timezone.now(),Blogs=blogId, comment=comment)
        return newComment
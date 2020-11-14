from django.db import models

# Create your models here.
class Blogs(models.Model):
    title_text = models.CharField(max_length=100)
    content_text = models.CharField()
    blogScore = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

class Comment(models.Model):
    Blogs = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    comment_text = models.CharField()
    commentScore = models.IntegerField(default=0)
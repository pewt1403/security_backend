from django.db import models

# Create your models here.
class Blogs(models.Model):
    title_text = models.CharField(max_length=100)
    content_text = models.CharField(max_length=2100)
    blogScore = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    @classmethod
    def create(cls, title, content):
        blog = cls(title_text=title, content_text=content, blogScore=0, )
        return blog

class Comment(models.Model):
    Blogs = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    creator = models.CharField(max_length=30)
    pub_date =  models.DateTimeField('date published')
    comment_text = models.CharField(max_length=700)
    commentScore = models.IntegerField(default=0)

    @classmethod
    def create(cls, comment):
        return
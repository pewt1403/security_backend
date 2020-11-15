from django.utils import timezone
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=30)
    content = models.CharField(max_length=2100)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    edited = models.BooleanField(default=False)

    # @classmethod
    # def has_perm_edit(self, user):
    #     print(user.username, self.creator)
    #     if user.id == self.pk:
    #         return True
    #     else:
    #         return False

    @classmethod
    def create(cls, title, content, creator):
        blog = cls(title=title, creator=creator, content=content, score=0, pub_date= timezone.now())
        return blog

class Comment(models.Model):
    Blogs = models.ForeignKey(Blog, on_delete=models.CASCADE)
    creator = models.CharField(max_length=30)
    pub_date =  models.DateTimeField('date published')
    comment = models.CharField(max_length=700)
    score = models.IntegerField(default=0)

    @classmethod
    def create(cls, comment, blogId, creator):
        newComment = cls(Blogs=blogId, creator= creator, pub_date=timezone.now(), comment=comment, score=0 )
        return newComment
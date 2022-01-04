from django.db import models
from django.db.models.base import Model

# Create your models here.


class User(models.Model):
    pass




class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    views = models.PositiveIntegerField(default=0)
    is_promote = models.BooleanField(default=False)
    date = models.DateField()
    # content = 
    # comments = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Comment(models.Model):
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('Comment')
    child = models.ForeignKey('Comment')
    is_valid = models.BooleanField(default=False)
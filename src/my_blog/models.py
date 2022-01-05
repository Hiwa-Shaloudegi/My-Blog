from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=50)
    content = models.TextField(null=True) # content = Text Editor
    summary = models.TextField(null=True)
    views = models.PositiveIntegerField(default=0)
    is_promote = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    image_name = models.CharField(max_length=64, null=True)
    slug = models.SlugField(unique=True, db_index=True, null=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    # parent = models.ForeignKey('Comment', on_delete=models.CASCADE) 
    # child = models.ForeignKey('Comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", null=True)
    content = models.TextField(null=True)   # content = Text Editor
    date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post}'






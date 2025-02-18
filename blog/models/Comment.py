from django.db import models
from blog.models import Post
from django.contrib.auth.models import User

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post')
    content = models.TextField()
    note = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.content
    
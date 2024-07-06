from django.db import models
from django.contrib.auth.models import User
from blog.models import Category
from blog.models import Tag
from django.utils.text import slugify



class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    
    #OneToMany, ManyToOne
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #OneToMany, ManyToOne
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag')
    image = models.ImageField(upload_to='posts/%Y/%m/%d', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
            return self.title
        
    def save(self, *args, **kwargs):
        if not self.slug:
                self.slug = slugify(self.title)
        super().save(*args, **kwargs)
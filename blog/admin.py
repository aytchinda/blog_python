from django.contrib import admin
from blog.models import Category
from blog.models import Tag, Post, Comment, Contact, Profile

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Profile)

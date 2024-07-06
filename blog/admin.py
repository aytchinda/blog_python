from django.contrib import admin
from blog.models import Category
from blog.models import Tag, Post, Comment, Contact, Profile



class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author','category','is_published', 'created_at', 'updated_at')
    list_filter = ('is_published','category', 'tags')
    list_editable = ('is_published', )
    list_per_page = 10
    list_max_show_all = 100
    search_fields = ('title', 'content', 'author__username', 'category__name')
    
# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Profile)

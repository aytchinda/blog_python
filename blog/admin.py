from django.contrib import admin
from django.urls import reverse

from django.utils.html import format_html
from blog.models import Category, Tag, Post, Comment, Contact, Profile

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_title', 'author', 'category', 'is_published', 'created_at', 'updated_at','display_tags_count', 'display_actions')
    list_filter = ('is_published', 'category', 'tags')
    # list_editable = ('is_published',)
    list_per_page = 10
    list_max_show_all = 100
    search_fields = ('title', 'content', 'author__username', 'category__name')

    def display_tags_count(self, post):
        return post.tags.count()
   
    def display_title(self, post):
        no_icon = '❌'
        yes_icon = '✅'
        if post.is_published:
            title = '<span style = "color:green">'+ post.title +'</span>'
            return format_html(yes_icon + title)
        else:
            title = '<span style = "color:red">'+ post.title +'</span>'
            return format_html(no_icon + title)
        
    def display_actions(self, post):
        return  format_html(
            '<a href="{}" class="addlink">View</a>&nbsp;'
            '<a href="{}" class="addlink">Edit</a>&nbsp;'
            '<a href="{}" class="addlink">Delete</a>&nbsp;',
             reverse('admin:blog_post_change', args=[post.id]),
             reverse('admin:blog_post_change', args=[post.id]),
            reverse('admin:blog_post_delete', args=[post.id]),
            )
    
    display_tags_count.short_description = 'Tags'
    display_actions.short_description = 'Actions'
    display_title.short_description = 'Title'




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at',)
    list_per_page = 10
    list_max_show_all = 100
    search_fields = ('name', 'description',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at',)
    list_editable = ('description',)
    list_per_page = 10
    list_max_show_all = 100
    search_fields = ('name', 'description',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'note', 'created_at',)
    list_filter = ('created_at', 'updated_at', 'author',)
    list_per_page = 10
    list_max_show_all = 100
    search_fields = ('author__username', 'content',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('civility', 'name', 'email', 'subject', 'message', 'created_at')
    list_filter = ('created_at', 'name', 'email', 'subject')
    list_editable = ('civility',)
    list_display_links = ('name',)
    list_per_page = 10
    list_max_show_all = 100
    search_fields = ('name', 'email', 'subject')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('description', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'user',)
    list_per_page = 10
    list_max_show_all = 100
    search_fields = ('user',)

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Profile, ProfileAdmin)

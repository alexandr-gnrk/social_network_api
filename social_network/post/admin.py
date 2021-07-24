from django.contrib import admin
from .models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'likes', 'created')
    list_filters = ('created',)

@admin.register(Like)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'date')
    list_filters = ('date',)

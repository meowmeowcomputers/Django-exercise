from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import Blog, Post
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'created', 'blog')

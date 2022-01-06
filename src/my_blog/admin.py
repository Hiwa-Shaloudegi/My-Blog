from django.contrib import admin
from django.db.models.base import Model
from tinymce.widgets import TinyMCE 
from django.db import models

from .models import Comment, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)} # <slug> automaticly will be filled based on <title>

    formfield_overrides = {
        models.TextField:{'widget':TinyMCE()}
    }

class CommentAdmin(admin.ModelAdmin):
        formfield_overrides = {
        models.TextField:{'widget':TinyMCE()}
    }


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
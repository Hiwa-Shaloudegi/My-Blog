from django.contrib import admin
from .models import Comment, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)} # <slug> automaticly will be filled based on <title>


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
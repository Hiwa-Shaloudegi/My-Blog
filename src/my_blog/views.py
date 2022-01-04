from django.shortcuts import render

from .models import User, Post, Comment

# Create your views here.

def index(request):
    return render(request, 'my_blog/index.html', context={
        
    })
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import User, Post, Comment

# Create your views here.

def index(request):
    posts = Post.objects.all()
    # paginator = Paginator(posts, 10)
    
    return render(request, 'my_blog/index.html', context={
        'posts':posts
    })



def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    comments = post.comments.filter(active=True)
    return render(request, 'my_blog/post_detail.html', context={
        'post':post,
        'comments':comments
    })
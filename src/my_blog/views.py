from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import User, Post, Comment

    
def index(request):
    posts = Post.objects.all().order_by("-date")
    # paginator = Paginator(posts, 10)
    latest_posts = posts[:5]
    most_viewd_posts = posts.order_by("-views")[:5]
    promoted_posts = Post.objects.all().filter(is_promote=True)[:3]   # ERROR: negative ...
    
    return render(request, 'my_blog/index.html', context={
        'posts':posts,
        'latest_posts':latest_posts,
        'most_viewd_posts':most_viewd_posts,
        'promoted_posts':promoted_posts,
    })




def posts(request):
    posts = Post.objects.all().order_by("-date")
    most_viewd_posts = posts.order_by("-views")
    # most_comment_posts = Post.comments.all().order_by()
    # Post.objects.all().filter(title__contains='')

    return render(request, 'my_blog/posts.html', context={
        "posts":posts,
        'most_viewd_posts':most_viewd_posts,
        
    })




def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)

    return render(request, 'my_blog/post_detail.html', context={
        'post':post,
        'comments':comments,
    })
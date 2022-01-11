from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from .models import User, Post, Comment

    
def index(request):
    posts = Post.objects.all().order_by("-date")
    # paginator = Paginator(posts, 10)
    latest_posts = posts[:5]
    most_viewd_posts = posts.order_by("-views")[:5]
    promoted_posts = Post.objects.all().filter(is_promote=True)[:3]   
    
    return render(request, 'my_blog/index.html', context={
        'posts':posts,
        'latest_posts':latest_posts,
        'most_viewd_posts':most_viewd_posts,
        'promoted_posts':promoted_posts,
    })




def posts(request):
    posts = Post.objects.all().order_by("-date")
    latest_posts = posts[:5]
    most_viewd_posts = posts.order_by("-views")[:5]
    all_most_viewd_posts = posts.order_by("-views")
    all_most_commented_posts = Post.objects.annotate(num_comment=Count('comments')).order_by('-num_comment') 
    # Post.objects.all().filter(title__contains='')

    return render(request, 'my_blog/posts.html', context={
        "posts":posts,
        'latest_posts':latest_posts,
        'most_viewd_posts':most_viewd_posts,
        'all_most_viewd_posts':all_most_viewd_posts,
        'all_most_commented_posts':all_most_commented_posts,
        
    })




def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-date")

    if request.method == "POST":
        author_username = request.session['user']
        author = get_object_or_404(User, username=author_username)

        content = request.POST.get('content')

        comment = Comment(content=content, author=author, post=post)
        comment.save()
        messages.success(request, "Comment Added")

        return redirect('post_detail', slug=slug) 


    return render(request, 'my_blog/post_detail.html', context={
        'post':post,
        'comments':comments,
    })
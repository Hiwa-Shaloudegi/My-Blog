from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from .models import User, Post, Comment

    
def index(request):
    posts = Post.objects.all().order_by("-date")

    # --Paginator-- #
    paginator = Paginator(posts, 2) 
    page = request.GET.get('page')   
    paginator_posts = paginator.get_page(page)  

    latest_posts = posts[:5]
    most_viewd_posts = posts.order_by("-views")[:5]
    promoted_posts = Post.objects.all().filter(is_promote=True)[:3]   
    
    return render(request, 'my_blog/index.html', context={
        'posts':posts,
        'paginator_posts':paginator_posts,
        'latest_posts':latest_posts,
        'most_viewd_posts':most_viewd_posts,
        'promoted_posts':promoted_posts,
    })




def posts(request):
    posts = Post.objects.all().order_by("-date")

    # --Paginator-- #
    paginator = Paginator(posts, 2) 
    page = request.GET.get('page')   
    paginator_posts = paginator.get_page(page)  

    latest_posts = posts[:5]
    all_most_viewd_posts = posts.order_by("-views")
    most_viewd_posts = all_most_viewd_posts[:5]
    all_most_commented_posts = Post.objects.annotate(num_comment=Count('comments')).order_by('-num_comment')


    if request.method == "POST" and 'btnform1' in request.POST:
        search = request.POST.get('search')
        searched_posts = Post.objects.filter(
            Q(title__contains=search) |
            Q(summary__contains=search) |
            Q(content__contains=search)
            )

        return render(request, 'my_blog/posts.html', context={
            'searched_posts':searched_posts,
            'search':search,
            'posts':posts,
            'latest_posts':latest_posts,
        })



    if request.method == "POST" and 'btnform2' in request.POST: 
        view_min = request.POST.get('view_min') 
        view_max = request.POST.get('view_max')

        filtered_views_posts = Post.objects.filter(views__gte=view_min)
        filtered_views_posts = filtered_views_posts.filter(views__lte=view_max)

        return render(request, 'my_blog/posts.html', context={
            'filtered_views_posts':filtered_views_posts,
            'view_min':view_min,
            'view_max':view_max,
            'posts':posts,
            'latest_posts':latest_posts,
        })



    if request.method == "POST" and 'btnform3' in request.POST: 
        date_min = request.POST.get('date_min') 
        date_max = request.POST.get('date_max')

        filtered_posts = Post.objects.filter(date__gte=date_min)
        filtered_posts = filtered_posts.filter(date__lte=date_max)

        return render(request, 'my_blog/posts.html', context={
            'filtered_posts':filtered_posts,
            'date_min':date_min,
            'date_max':date_max,
            'posts':posts,
            'latest_posts':latest_posts,
        })

    
    return render(request, 'my_blog/posts.html', context={
        "posts":posts,
        'paginator_posts':paginator_posts,
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
        comment.parent = comment
        comment.save()
        messages.success(request, "Comment Added")

        return redirect('post_detail', slug=slug) 


    return render(request, 'my_blog/post_detail.html', context={
        'post':post,
        'comments':comments,
    })
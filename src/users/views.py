from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate 
from django.utils.text import slugify
from django.core.paginator import Paginator



from my_blog.models import Comment, Post, User

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user'] = user.username 
            messages.success(request, f"{user.username} Account Created")
            return redirect('profile', username=user.username)
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', context={
        'form':form,
    })




def login(request):
    if 'user' in request.session:  # if a user is logged in and opens a login page(by typing url /login), it will be redirected to the profile page
        return redirect('profile', username=request.session['user'])

    if request.method == "POST":

        username = request.POST.get('username') 
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        # user = User.objects.all().filter(username=username)     # WTF!: empty list?? # , password__exact=password

        if user is not None:    # user.exists()
            request.session['user'] = username                
            messages.info(request, f"You are loged in as {username}")
            return redirect('profile', username=username)

        else:
            messages.warning(request, "Invalid username or password! please try again")
            return redirect('login')

    return render(request, 'users/login.html')



def logout(request):
    del request.session['user']
    messages.info(request, "Logged out successfully!")
    return redirect('index')



def profile(request, username):
    cuurent_user = request.session['user']
    url_username = request.path.split('/') 

    if url_username[-1] == cuurent_user:          
        author = get_object_or_404(User, username=username)
        author_posts = author.posts.all().order_by('-date') 

        # --Paginator-- #
        paginator = Paginator(author_posts, 2) 
        page = request.GET.get('page')   
        paginator_posts = paginator.get_page(page)  
       
        return render(request, 'users/profile.html', context={
            'author':author,
            'author_posts':author_posts,
            'paginator_posts':paginator_posts,

        })

    else:
        return redirect('login')






def add_post(request):
    if 'user' not in request.session:  # if a user is Not logged in and opens add_post page(by typing url /add_post), it will be redirected to the index page
        return redirect('index')

    if request.method == "POST":

        title = request.POST.get('title')
        summary = request.POST.get('summary') 
        content = request.POST.get('content')
        author_username = request.session['user']
        author = get_object_or_404(User, username=author_username)
        slug = slugify(title)

        post = Post(title=title, summary=summary, content=content, author=author, image_name='default.png', slug=slug)
        post.save()

        messages.success(request, "Post Added")
        return redirect('profile', username=author)


    return render(request, 'users/add_post.html', context={

    })



def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    user = post.author

    if 'user' not in request.session or request.session['user'] != user.username:  # if a user is Not logged in and opens delete_post page(by typing url /delete_post/id), it will be redirected to the index page
        return redirect('index')

    if request.method == "POST":    
        post.delete()
        messages.success(request, "Post Deleted")
        return redirect('profile', username=user.username)

    return render(request, 'users/delete_post.html', context={
        'post':post,
        'user':user.username
    })




def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    user = post.author

    if 'user' not in request.session or request.session['user'] != user.username:  # if a user is Not logged in and opens edit_post page(by typing url /edit_post/id), it will be redirected to the index page
        return redirect('index')
    
    if request.method == "POST":

        title = request.POST.get('title')
        summary = request.POST.get('summary') 
        content = request.POST.get('content')
        author_username = request.session['user']
        author = get_object_or_404(User, username=author_username)
        slug = slugify(title)

        post.title = title
        post.summary = summary
        post.content = content
        post.author = author
        post.slug = slug
        
        post.save()

        messages.success(request, "Post Edited")
        return redirect('profile', username=author)

    return render(request, 'users/edit_post.html', context={
        'post':post,
    })



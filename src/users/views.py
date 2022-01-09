from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate 

from my_blog.models import User

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
            return redirect('users/login.html')

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
        author_posts = author.posts.all() 
       
        return render(request, 'users/profile.html', context={
            'author':author,
            'author_posts':author_posts,
        })

    else:
        return redirect('login')

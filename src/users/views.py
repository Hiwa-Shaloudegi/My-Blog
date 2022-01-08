from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate 

from my_blog.models import User

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user'] = user.id
            # username = form.cleaned_data.get('username')
            messages.success(request, f"{user.username} Account Created")
            return redirect("index")
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', context={
        'form':form,
    })




def login(request):
    if request.method == "POST":
        username = request.POST.get('username') 
        password = request.POST.get('password')

        # form = AuthenticationForm(data=request.POST)
        # if form.is_valid():
        #     request.session['user'] = form.get_user().id
        #     messages.info(request, f"You are loged in as {username}")  # {form.get_user().username}
        #     return redirect('index') 
        # else:
        #     messages.warning(request, "Invalid username or password! please try again")

        user = authenticate(username=username, password=password)
        # user = User.objects.all().filter(username=username)           # WTF!: empty list?? # , password__exact=password

        if user is not None:       # user.exists()
            request.session['user'] = user.id                           # request.session['user'] = username
            messages.info(request, f"You are loged in as {username}")
            return redirect('index') # return redirect('profile')
        else:
            messages.warning(request, "Invalid username or password! please try again")
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')



def logout(request):
    del request.session['user']
    messages.info(request, "Logged out successfully!")
    print("Logged out successfully!")

    return redirect('index')

    


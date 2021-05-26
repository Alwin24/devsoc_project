from django.shortcuts import render, redirect
from authentication.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == 'POST':
        f = SignUpForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return render(request,'signup.html')

    else:
        f = SignUpForm()
    
    return render(request,'signup.html')



# def loginform(request):

#     return render(request,'loginform.html')

def login(request):
    if request.user.is_authenticated:
        print("authentication=true") 
        return render(request,'main.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            print('user is not none')
            # correct username and password login the user
            auth.login(request, user)
            print("success in loggin in")
            return redirect('home')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request,'login.html')

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'main.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

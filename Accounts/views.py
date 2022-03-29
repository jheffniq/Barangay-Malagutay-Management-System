from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import User_form

def LoginUser (request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Logged in Succesfully!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again")
            return redirect('/login/')

    else:
        return render(request,"login.html")


def LogoutUser (request):
    logout(request)
    return redirect('/index/')

def Guestuser (request):
    return render(request,"guest/home.html")


def Adduser(request):
    if request.method == "POST":
        form = User_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request, "User sucessfully added")
            return redirect('/users/')
    else:
        form = User_form

    context = {
        'form' : form
    }

    return render(request, "register.html", context = context)

@login_required(login_url='login')
def Displayusers (request):
    User = get_user_model()
    users = User.objects.all()
    context = {
        "user" : users
    }
    return render(request, "users.html", context = context)


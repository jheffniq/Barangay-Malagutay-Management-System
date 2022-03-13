from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
    return redirect('/login/')



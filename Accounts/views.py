from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import User_form, Update_user, OfficalForm
from .models import Official

def LoginUser (request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,"Logged In Succesfully!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password. Please try again")
                return redirect('/login/')

        else:
            return render(request,"login.html")
    else:
        return redirect('/home/')

def LogoutUser (request):
    logout(request)
    messages.success(request, "Logged Out Succesfully")
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

def Edituser(request):
    if request.method == "POST":
        form = Update_user(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "User sucessfully updated")
            return redirect('/users/')
        def get_object(self):
            return self.request.user
    
    else:
        form = Update_user(instance=request.user)

    context = { 
        'form' : form
    }

    return render(request, "edit_user.html", context = context)


@login_required(login_url='login')
def Displayusers (request):
    User = get_user_model()
    users = User.objects.all()

    Current_user = request.user
    if Current_user.is_superuser:
        admin = True
    else:
        admin = False

    context = {
        "user" : users,
        "admin" : admin,
    }
    return render(request, "users.html", context = context)

def Edit_officals(request):
   Officials_obj = Official.objects.get(id=1)
   Councilors1 = Officials_obj.Barangay_Councilors.replace('','').split(',')
   Councilors2 = Officials_obj.SK_Councilors.replace('','').split(',')

   form = OfficalForm(instance=Officials_obj)
   if request.method == "POST":
        form = OfficalForm(request.POST, instance = Officials_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "List Of Officials Have Been Updated")
            return redirect('users')
            
   context = {'form' : form, 'Councilors1' : Councilors1}
   return render(request,"officials_form.html",context = context)

def Deleteuser(request, pk):
    User = get_user_model()
    userdel = User.objects.get(id = pk)
    userdel.delete()
    messages.success(request, "User successfully deleted")
    return redirect('/users/')
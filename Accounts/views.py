import profile
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Profileform, User_form, Update_user, OfficalForm
from .models import Official, Profile

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

@login_required(login_url='login')
def LogoutUser (request):
    logout(request)
    messages.success(request, "You have been signed out")
    return redirect('/index/')


def Guestuser (request):
    Officials_obj = Official.objects.get(id=1)
    Councilors1 = Officials_obj.Barangay_Councilors.replace('','').split(',')
    Councilors2 = Officials_obj.SK_Councilors.replace('','').split(',')

    context = {
        'Officials_obj' : Officials_obj,
        'Councilors1' : Councilors1,
        'Councilors2' : Councilors2
    }
    return render(request,"guest/home.html", context = context)

def Faqs (request):
    return render(request, "guest/faq.html")


@login_required(login_url='login')
def Adduser(request):
    if request.method == "POST":
        form = User_form(request.POST)
        details = Profileform(request.POST)
        if form.is_valid() and details.is_valid():
            user = form.save()
            profile = details.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request, "User sucessfully added")
            return redirect('/users/')
    else:
        form = User_form()
        details = Profileform()

    context = {
        'form' : form,
        'details' : details
    }

    return render(request, "register.html", context = context)

@login_required(login_url='login')
def Edituser(request):

    NoPosition = False
    try:
        prof = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        NoPosition = True

    if request.method == "POST":
        form = Update_user(request.POST, instance=request.user)
        if NoPosition == True:
            details = Profileform(request.POST)
        else:
            details = Profileform(request.POST, instance=prof)

        if form.is_valid():
            form.save()
            details.save()

            messages.success(request, "User sucessfully updated")
            return redirect('/users/')
        def get_object(self):
            return self.request.user
    
    else:
        form = Update_user(instance=request.user)
        if NoPosition == True:
            details = Profileform()
        else:
            details = Profileform(instance=prof)

    context = { 
        'form' : form,
        'details' : details
    }

    return render(request, "edit_user.html", context = context)


@login_required(login_url='login')
def Displayusers (request):
    User = get_user_model()
    users = User.objects.all()
    positions = Profile.objects.all()

    Current_user = request.user
    if Current_user.is_superuser:
        admin = True
    else:
        admin = False

    context = {
        "user" : users,
        "admin" : admin,
        "Current_user" : Current_user,
        'positions' : positions
    }
    return render(request, "users.html", context = context)


@login_required(login_url='login')
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

@login_required(login_url='login')
def Deleteuser(request, pk):
    User = get_user_model()
    userdel = User.objects.get(id = pk)
    userdel.delete()
    messages.success(request, "User successfully deleted")
    return redirect('/users/')
    #
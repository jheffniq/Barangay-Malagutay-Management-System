from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.db.models import Q
from .models import Resident
from .forms import Resident_Form

def view_404(request, exception=None):
    return redirect('/home/')


#Display Resident
def Display_resident (request):

    Resident_obj = Resident.objects.all()

    context = {
        'Resident_obj' : Resident_obj,
    }

    return render (request,"Residents.html",context = context)

#Display Profile

def Display_profile(request, pk):
    resident_obj = Resident.objects.get(id = pk)

    context = {
        "profile" : resident_obj
    }
    return render(request, "resident_profile.html",context=context)


#Create Resident
def Create_resident(request):
    form = Resident_Form()

    if request.method == "POST":
        form = Resident_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Resident has been added")
            return redirect('/residents')


    context = {
        'form':form
    }

    return render(request,"profile_form.html",context=context)

#Update Resident  
def Update_resident(request, pk):
    resident_obj = Resident.objects.get(id = pk)
    form = Resident_Form(instance = resident_obj)
    if request.method == "POST":
        form = Resident_Form(request.POST, request.FILES, instance = resident_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Resident has been modified")
            return redirect('/residents/')

    context = {
        'form' : form
    }

    return render(request,"profile_form.html",context = context)

#Delete Resident
def Delete_resident(request, pk):
    resident_obj = Resident.objects.get(id = pk)
    resident_obj.delete()
    messages.success(request, "Resident has been deleted")
    return redirect('/residents/')

#Search
def Search_resident(request):
    if request.method == "POST":
        q = request.POST["q"]
        Name_query = Q(Q(First_name__icontains = q) | Q(Middle_name__icontains = q) | Q(Last_name__icontains = q))
        result = Resident.objects.filter(Name_query)
        return render(request, "Search_resident.html",{'result': result,'q':q})

    else:
        return render(request, "Search_resident.html")

def home(request):
    Males = Resident.objects.filter(Gender = "Male").count()
    Females = Resident.objects.filter(Gender= "Female").count()

    context = {
        'Males' : Males,
        'Females' : Females
    }
    return render(request,"home.html",context = context)


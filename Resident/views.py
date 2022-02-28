from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Resident
from .forms import Resident_Form


def home(request):

    return render(request,"base.html")

#Display Resident
def Display_resident (request):
    Resident_obj = Resident.objects.all()
    Resident_obj2 = Resident.objects.get(id = 6)


    context = {
        'Resident_obj' : Resident_obj,
        'Res2' : Resident_obj2,
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


from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Resident
from .forms import Resident_Form


def home(request):

    return render(request,"base.html")

def Display_resident (request):
    Resident_obj = Resident.objects.all()
    Resident_obj2 = Resident.objects.get(id = 6)


    context = {
        'Resident_obj' : Resident_obj,
        'Res2' : Resident_obj2,
    }

    return render (request,"Residents.html",context = context)

def Create_resident(request):
    form = Resident_Form()

    if request.method == "POST":
        form = Resident_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/residents')

    context = {
        'form':form
    }

    return render(request,"profile_form.html",context=context)
    
def Update_resident(request, pk):
    resident_obj = Resident.objects.get(id = pk)
    form = Resident_Form(instance = resident_obj)
    if request.method == "POST":
        form = Resident_Form(request.POST, request.FILES, instance = resident_obj)
        if form.is_valid():
            form.save()
            return redirect('/residents')

    context = {
        'form' : form
    }

    return render(request,"profile_form.html",context = context)
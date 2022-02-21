from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Resident
from .forms import Resident_Form


def home(request):

    return render(request,"base.html")

def Display_resident (request):
    Resident_obj = Resident.objects.all()


    context = {
        'Resident_obj' : Resident_obj,
    }

    return render (request,"Residents.html",context = context)

def formm(request):
    form = Resident_Form(request.POST)
    if form.is_valid():
        form.save(commit = False)

    else:
        form = Resident_Form()
    context = {
        'form':form
    }

    return render(request,"profile_form.html",context)
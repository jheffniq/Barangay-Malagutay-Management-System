from django.shortcuts import render, redirect
from Resident.models import Resident
from .models import Blotreport
from .forms import Blotter_Form
from django.contrib import messages
from django.db.models import Q

def Addreport(request):
    Resident_obj = Resident.objects.all()
    context = {
        "Resident_obj" : Resident_obj
    }
    return render(request,"blotter/Blotter_register.html",context = context)

def Blotter_search_resident(request):
    if request.method == "POST":
        q = request.POST["q"]
        Name_query = Q(Q(First_name__icontains = q) | Q(Middle_name__icontains = q) | Q(Last_name__icontains = q))
        result = Resident.objects.filter(Name_query)
        return render(request, "blotter/Search_resident.html",{'result': result,'q':q})

    else:
        return render(request, "blotter/Search_resident.html")

def Create_Report(request, pk):
    form = Blotter_Form()

    if request.method == "POST":
        Resident_obj = Resident.objects.get(id = pk)
        Resident_obj.Blacklisted =  True
        form = Blotter_Form(request.POST)
        if form.is_valid():
            form.save()
            Blotobj = Blotreport.objects.last()
            Blotobj.Offender = Resident_obj
            Blotobj.save()
            Resident_obj.save()
            messages.success(request, "Blotter report has been added")
            return redirect('/add_report/')

    context = {
        'form':form
    }

    return render(request,"blotter/blotter_form.html",context=context)

def Blotter_display(request):
    Blotter_obj = Blotreport.objects.all()
    context = {
        'Botter_obj' : Blotter_obj
    }
    return render(request, "blotter/blotter_display.html", context = context)

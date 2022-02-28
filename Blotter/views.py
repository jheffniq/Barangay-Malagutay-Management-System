from django.shortcuts import render
from Resident.models import Resident
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

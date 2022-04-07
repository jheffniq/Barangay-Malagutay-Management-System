from cmath import log
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Resident, CSV
from .forms import Resident_Form, CSVmodel
import csv
from datetime import datetime

def view_404(request, exception=None):
    return redirect('/index/')


#Display Resident
@login_required(login_url='login')
def Display_resident (request):
    Resident_obj = Resident.objects.all()

    form = CSVmodel(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        form = CSVmodel

        csv_obj = instance
        with open(csv_obj.file_name.path,'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    first_name = row[1]
                    middle_name = row[2]
                    last_name = row[3]

                    birthdate = datetime.strptime(row[4], "%m/%d/%Y").strftime("%Y-%m-%d")

                    gender = row[5]
                    mstatus = row[6]
                    contact = row[7]
                    citizenship = row[8]
                    religion = row[9]
                    occupation = row[10]
                    vacstatus = row[11]
                    address = row[12]

                    Resident.objects.create(
                    First_name = first_name,
                    Middle_name = middle_name,
                    Last_name = last_name,
                    Birthdate = birthdate,
                    Gender = gender,
                    Contact = contact,
                    Marital_status = mstatus,
                    Citizenship = citizenship,
                    Religion = religion,
                    Occupation = occupation,
                    Vaccination = vacstatus,
                    Address = address
                     )
        csv_obj.activated = True
        csv_obj.save()
        return redirect('/residents/')

    context = {
        'Resident_obj' : Resident_obj,
        'form' : form
    }

    return render (request,"Residents.html",context = context)

#Display Profile
@login_required(login_url='login')
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
@login_required(login_url='login')
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
@login_required(login_url='login')
def Delete_resident(request, pk):
    resident_obj = Resident.objects.get(id = pk)
    resident_obj.delete()
    messages.success(request, "Resident has been deleted")
    return redirect('/residents/')

#Search
@login_required(login_url='login')
def Search_resident(request):
    if request.method == "POST":
        q = request.POST["q"]
        searched = True
        Name_query = Q(Q(First_name__icontains = q) | Q(Middle_name__icontains = q) | Q(Last_name__icontains = q))
        result = Resident.objects.filter(Name_query)
        return render(request, "Search_resident.html",{'result': result,'q':q,'searched':searched})

    else:
        searched = False
@login_required(login_url='login')
def home(request):
    Males = Resident.objects.filter(Gender = "Male").count()
    Females = Resident.objects.filter(Gender= "Female").count()

    context = {
        'Males' : Males,
        'Females' : Females
    }
    return render(request,"home.html",context = context)

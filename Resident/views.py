from cmath import log
from re import A
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.mail import EmailMessage
from .models import Resident, CSV
from Resident.models import TempResident
from Blotter.models import Blotreport
from .forms import Resident_Form, CSVmodel, Temp_Form
from Certification.models import Certrequest
import csv
from datetime import datetime, date
from django import forms
from django.core.files.storage import default_storage
import secrets

def view_404(request, exception=None):
    return redirect('/index/')

#Display Resident
@login_required(login_url='login')
def Display_resident (request):
    Resident_obj = Resident.objects.all()
    code = secrets.token_hex(5)



    form = CSVmodel(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        form = CSVmodel


        csv_obj = instance
        filename = str(csv_obj.file_name)
        with default_storage.open(filename,'r') as f:
            decoded_file = f.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)

            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else: 
                    
                    while True:
                        if Resident.objects.filter(Resident_code = code).exists():
                            code = secrets.token_hex(5)
                        else:
                            break

                    first_name = row[1]
                    middle_name = row[2]
                    last_name = row[3]

                    birthdate = datetime.strptime(row[4], "%m/%d/%Y").strftime("%Y-%m-%d")

                    gender = row[5]
                    mstatus = row[6]
                    Philhealth = row[7]
                    email = row[8]
                    contact = row[9]
                    citizenship = row[10]
                    religion = row[11]
                    occupation = row[12]
                    vacstatus = row[13]
                    address = row[14]

                    Resident.objects.create(
                    First_name = first_name,
                    Middle_name = middle_name,
                    Last_name = last_name,
                    Birthdate = birthdate,
                    Gender = gender,
                    Contact = contact,
                    Philhealth_membership = Philhealth,
                    Marital_status = mstatus,
                    Citizenship = citizenship,
                    Religion = religion,
                    Occupation = occupation,
                    Vaccination = vacstatus,
                    Address = address,
                    Email = email,
                    Resident_code = code
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
@login_required(login_url='login')
def Create_resident(request):
    form = Resident_Form()

    if request.method == "POST":
        form = Resident_Form(request.POST, request.FILES)
        code = secrets.token_hex(5)

        #Check for duplicates
        while True:
            if Resident.objects.filter(Resident_code = code).exists():
                code = secrets.token_hex(5)
            else:
                break

        if form.is_valid():
            Resobj = form.save(commit=False)
            Resobj.Resident_code = code
            Resobj.save()
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

#Home
@login_required(login_url='login')
def home(request):
    today = date.today()
    Resident_obj = Resident.objects.all()
    TotResident = Resident.objects.all().count()
    TotBlot = Blotreport.objects.all().count()
    Regreq = TempResident.objects.all()
    Regreqs = Regreq.count()
    Certreq = Certrequest.objects.all().count()
    Males = Resident.objects.filter(Gender = "Male").count()
    Females = Resident.objects.filter(Gender= "Female").count()
    Vaccinated = Resident.objects.filter(Vaccination = "Vaccinated").count()
    Unvaccinated = Resident.objects.filter(Vaccination = "Unvaccinated").count()
    phNone = Resident.objects.filter(Philhealth_membership = "None").count()
    PhEmployed = Resident.objects.filter(Philhealth_membership = "Employed").count()
    PhVoluntary = Resident.objects.filter(Philhealth_membership = "Voluntary").count()
    PhOfw = Resident.objects.filter(Philhealth_membership = "OFW").count()
    PhSponsored = Resident.objects.filter(Philhealth_membership = "Sponsored").count()
    PhIndigent = Resident.objects.filter(Philhealth_membership = "Indigent").count()
    PhLifetime = Resident.objects.filter(Philhealth_membership = "Lifetime").count()
    PhSenior = Resident.objects.filter(Philhealth_membership = "Senior").count()
    Single = Resident.objects.filter(Marital_status = "Single").count()
    Married = Resident.objects.filter(Marital_status = "Married").count()
    Separated = Resident.objects.filter(Marital_status = "Separated").count()
    Widowed = Resident.objects.filter(Marital_status = "Widowed").count()


    #Age distribution
    Kids = 0
    Teens = 0
    Adults = 0
    Senior_Citizens = 0

    for Res in Resident_obj:
        age = today.year - Res.Birthdate.year
        if age <= 13:
            Kids += 1
        if age > 13 and age <= 21:
            Teens += 1
        if age > 21 and age <= 59:
            Adults += 1
        if age >= 60:
            Senior_Citizens += 1

    context = {
        'Males' : Males,
        'Females' : Females,
        'TotResident' : TotResident,
        'TotBlot' : TotBlot,
        'Regreqs' : Regreqs,
        'Certreq' : Certreq,
        'Vaccinated': Vaccinated,
        'Unvaccinated' : Unvaccinated,
        'Kids' : Kids,
        'Teens' : Teens,
        'Adults' : Adults,
        'Senior_Citizens' : Senior_Citizens,
        'phNone' : phNone,
        'PhEmployed' : PhEmployed,
        'PhVoluntary' : PhVoluntary,
        'PhOfw' : PhOfw,
        'PhSponsored' : PhSponsored,
        'PhIndigent': PhIndigent,
        'PhLifetime': PhLifetime,
        'PhSenior': PhSenior,
        'Single': Single,
        'Married' : Married,
        'Separated' : Separated,
        'Widowed' : Widowed
    }
    return render(request,"home.html",context = context)

#Add Temp Resident
def Temp_Resident(request):
    form = Temp_Form()

    if request.method == "POST":
        form = Temp_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Form submitted succesfully")
            return redirect('/index/')


    context = {
        'form':form
    }

    return render(request,"guest/temp_form.html",context=context)

#Display registration requests
@login_required(login_url='login')
def display_registrations(request):
    Request_obj = TempResident.objects.all()
    context = {
        'Request_obj' : Request_obj
    }
    return render(request, "register_requests.html", context = context)

@login_required(login_url='login')
def registration_profile(request, pk):
    profile = TempResident.objects.get(id = pk)
    context = {
        'profile' : profile
    }
    return render(request, "temp_profile.html", context = context)

#Accept resident
@login_required(login_url='login')
def Acceptresident(request, pk):
    Input = TempResident.objects.get(id = pk)
    code = secrets.token_hex(5)

    #Check for duplicates
    while True:
        if Resident.objects.filter(Resident_code = code).exists():
            code = secrets.token_hex(5)
        else:
            break

    Resident.objects.create(
    First_name = Input.First_name,
    Middle_name = Input.Middle_name,
    Last_name = Input.Last_name,
    Birthdate = Input.Birthdate,
    Gender = Input.Gender,
    Email = Input.Email,
    Contact = Input.Contact,
    Marital_status = Input.Marital_status,
    Citizenship = Input.Citizenship,
    Religion = Input.Religion,
    Occupation = Input.Occupation,
    Vaccination = Input.Vaccination,
    Address = Input.Address,
    Resident_code = code
    )
    receiver = Input.Email
    email = EmailMessage(
        'Barangay Malagutay Certificate Request',
        f'Good Day,\n\nCongratulations! Your request for registration has been accepted. You are now registered on the Barangay Malagutay Management System and can now request for certifications. \n\n\n\n Your Resident code is: \n\n {code}\n\n\n\nIf you find any errors please do not hesitate to contact us.\n\n\nThis is an automated email, do not reply. Please contact the respected barangay officials/workers if you have inquiries.',
        'testbmms88@gmail.com',
        [receiver]
    )
    email.send()
    Input.delete()
    messages.success(request, "Resident successfully added!")
    return redirect('/display_registrations/')

#Decline resident
@login_required(login_url='login')
def Declineresident(request, pk):
    Input = TempResident.objects.get(id = pk)
    receiver = Input.Email
    email = EmailMessage(
        'Barangay Malagutay Certificate Request',
        'Good Day,\n\nUnfortunately, your request for registration has been declined. Please contact the barangay officials/representatives regarding this issue.\n\n\nThis is an automated email, do not reply. Please contact the respected barangay officials/workers if you have inquiries.',
        'testbmms88@gmail.com', 
        [receiver]
    )
    email.send()
    Input.delete()
    messages.success(request, "Request has been declined")
    return redirect('/display_registrations/')

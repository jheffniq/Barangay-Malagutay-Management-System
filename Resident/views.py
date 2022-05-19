from cmath import log
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.mail import EmailMessage
from .models import Resident, CSV, Household
from Resident.models import TempResident
from Blotter.models import Blotreport
from .forms import Resident_Form, CSVmodel, Temp_Form, HouseholdForm
from Certification.models import Certrequest
import csv
from datetime import datetime, date
from django import forms
from django.core.files.storage import default_storage
import secrets

def view_400(request, exception):
    return render(request,"err_templates/400.html", status=400)

def view_403(request, exception):
    return render(request,"err_templates/403.html", status=403)

def view_404(request, exception=None):
    return redirect('/index/')

def view_500(request):
    if request.user.is_authenticated:
        messages.error(request,"An unexpected error has occured")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request,"An unexpected error has occured")
        return redirect(request.META.get('HTTP_REFERER'))


#Display Resident
@login_required(login_url='login')
def Display_resident (request):
    Resident_obj = Resident.objects.all()
    code = secrets.token_hex(3)

    form = CSVmodel(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        form = CSVmodel


        csv_obj = instance
        filename = str(csv_obj.file_name)
        with default_storage.open(filename,'r') as f:
            try:
                decoded_file = f.read().decode('utf-8').splitlines()
            except UnicodeDecodeError:
                messages.error(request,"Please check if the file format is correct")
                return redirect('/residents/')

            check_file = csv.reader(decoded_file)
            reader = csv.reader(decoded_file)
            
            #File Checking
            for c, row in enumerate(check_file):
                if c == 0:
                    pass
                else:
                    try:
                        Checkrow1 = row[1]
                        Checkrow2 = row[2]
                        Checkrow3 = row[3]
                        Checkrow4 = datetime.strptime(row[4], "%m/%d/%Y").strftime("%Y-%m-%d")
                        Checkrow5 = row[5]
                        Checkrow6 = row[6]
                        Checkrow7 = row[7]
                        Checkrow8 = row[8]
                        Checkrow9 = row[9]
                        Checkrow10 = row[10]
                        Checkrow11 = row[11]
                        Checkrow12 = row[12]
                        Checkrow13 = row[13]
                        Checkrow14 = row[14]
                    except ValueError:
                        messages.error(request,"Please check if there are rows that have incorrect data")
                        return redirect('/residents/')

            #create objects

            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else: 
                    while True:
                        if Resident.objects.filter(Resident_code = code).exists():
                            code = secrets.token_hex(3)
                        else:
                            break

                    first_name = row[1].capitalize()
                    middle_name = row[2].capitalize()
                    last_name = row[3].capitalize()

                    birthdate = datetime.strptime(row[4], "%m/%d/%Y").strftime("%Y-%m-%d")

                    gender = row[5].capitalize()
                    mstatus = row[6].capitalize()
                    Philhealth = row[7].capitalize()
                    email = row[8]
                    contact = row[9]
                    citizenship = row[10].capitalize()
                    religion = row[11].capitalize()
                    occupation = row[12].capitalize()
                    vacstatus = row[13].capitalize()
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
            messages.success(request,"Residents have been successfully added")
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
    household_obj = Household.objects.all()
    for h in household_obj:
        member = h.Member.all()
        if h.Head == resident_obj:
            House = f"{h.HouseholdName} (Head)"
            break
        else:
            for m in member:
                if m == resident_obj:
                    House = h.HouseholdName
                    break
                else:
                    House = None

    context = {
        "profile" : resident_obj,
        "House" : House
        
    }
    return render(request, "resident_profile.html",context=context)


#Create Resident
@login_required(login_url='login')
def Create_resident(request):
    form = Resident_Form()

    if request.method == "POST":
        form = Resident_Form(request.POST, request.FILES)
        code = secrets.token_hex(3)

        #Check for duplicates
        while True:
            if Resident.objects.filter(Resident_code = code).exists():
                code = secrets.token_hex(3)
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
    if request.user.username == "admin":
        current_user = "Admin"
    else:
        current_user = f"{request.user.first_name} {request.user.last_name}"
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
        'current_user' : current_user,
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
        'Widowed' : Widowed,
        'today' : today
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
    code = secrets.token_hex(3)

    #Check for duplicates
    while True:
        if Resident.objects.filter(Resident_code = code).exists():
            code = secrets.token_hex(3)
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

@login_required(login_url='login')
def DisplayVaccinated(request):
    Resident_obj = Resident.objects.filter(Vaccination="Vaccinated")
    context = {
        'Resident_obj' : Resident_obj
    }
    return render(request,"Vaccinatedresidents.html",context = context)

def DisplayUnvaccinated(request):
    Resident_obj = Resident.objects.filter(Vaccination="Unvaccinated")
    context = {
        'Resident_obj' : Resident_obj
    }
    return render(request,"Unvaccinatedresidents.html",context = context)


#Households
def Createhousehold(request):
    form = HouseholdForm
    Household_obj = Household.objects.all()
    if request.method == "POST":
        form = HouseholdForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            
            if Household.objects.filter(Head = instance.Head).exists():
                messages.error(request,"Selected head already belongs to a household")
                return redirect('/createhousehold/')
            else:
                form.save()

            Household_obj=Household.objects.last()
            Members = Household_obj.Member.all()
            Numbers = Members.count()

            Last_Name = Household_obj.Head.Last_name
            Household_obj.HouseholdName = f"{Last_Name} Household"
            Household_obj.Number = Numbers
            Household_obj.save()
            messages.success(request,"Form Submitted")
            return redirect("/createhousehold/")

    context = {
        'form' : form
    }
    return render (request,"HouseholdForm.html",context = context)

#Update Household
def UpdateHousehold(request, pk):
    household_obj = Household.objects.get(id = pk)
    form = HouseholdForm(instance = household_obj)

    if request.method == "POST":
        form = HouseholdForm(request.POST, instance = household_obj)
        if form.is_valid():
            form.save()
            Member = household_obj.Member.all()
            Numbers = Member.count()
            household_obj.Number = Numbers
            household_obj.save()

            messages.success(request, "Household has been updated")
            return redirect('/householdlist/')

    context = {
        'form' : form
    }

    return render(request,"Householdform.html",context = context)

#Delete Household
def DeleteHousehold(request,pk):
    household_obj = Household.objects.get(id = pk)
    household_obj.delete()
    messages.success(request, "Household has been deleted")
    return redirect('/householdlist/')


def HouseholdList(request):
    Household_obj = Household.objects.all()
    form = HouseholdForm
    Number = []
    for num in Household_obj:
        Members = num.Member.all()
        Number.append(Members.count())

    context = {
        'Household' : Household_obj,
        'Number' : Number,
        'form' : form
    }
    return render(request,"Houselist.html",context=context)




#View Household
def ViewHousehold(request, pk):
    Household_obj = Household.objects.get(id=pk)
    Members = Household_obj.Member.all()
    context = {
        'Household' : Household_obj,
        'Members' : Members,
    }
    return render(request,"Householdinfo.html",context=context)

def redirtest(request):
    return redirect(request.META.get('HTTP_REFERER'))
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Resident.models import Resident
from .models import Blotreport, Evidences, BlotArchive
from .forms import Blotter_Form, Blotter_Form_Unregistered
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import secrets

#Add report
@login_required(login_url='login')
def Addreport(request):
    Resident_obj = Resident.objects.all()
    context = {
        "Resident_obj" : Resident_obj
    }
    return render(request,"blotter/Blotter_register.html",context = context)

#Search
@login_required(login_url='login')
def Blotter_search_resident(request):
    if request.method == "POST":
        q = request.POST["q"]
        Name_query = Q(Q(First_name__icontains = q) | Q(Middle_name__icontains = q) | Q(Last_name__icontains = q))
        result = Resident.objects.filter(Name_query)
        return render(request, "blotter/Search_resident.html",{'result': result,'q':q})

    else:
        return render(request, "blotter/Search_resident.html")

#Report Form
@login_required(login_url='login')
def Create_Report(request, pk):
    form = Blotter_Form()

    if request.method == "POST":
        Resident_obj = Resident.objects.get(id = pk)
        Resident_obj.Blacklisted =  True
        files = request.FILES.getlist('evidence')

        form = Blotter_Form(request.POST)
        if form.is_valid():
            form.save()
            Blotobj = Blotreport.objects.last()
            Blotobj.Offender = Resident_obj
            Blotobj.save()
            Resident_obj.save()

            for file in files:
                new_file = Evidences(
                    Report = Blotobj,
                    images = file
                )
                new_file.save()
            messages.success(request, "Blotter report has been added")
            return redirect('/add_report/')

    context = {
        'form':form
    }

    return render(request,"blotter/blotter_form.html",context=context)

@login_required(login_url='login')
def Create_Report_unregistered(request):
    form = Blotter_Form_Unregistered()
    if request.method == "POST":
        form = Blotter_Form_Unregistered(request.POST)
        files = request.FILES.getlist('evidence')
        if form.is_valid():
            form.save()
            Blotobj = Blotreport.objects.last()
            Blotobj.Unregistered = True
            Blotobj.save()
            for file in files:
                new_file = Evidences(
                    Report = Blotobj,
                    images = file
                )
                new_file.save()
            messages.success(request, "Blotter report has been added")
            return redirect('/add_report/')

    context = {
        'form':form
    }

    return render(request,"blotter/blotter_form.html",context=context)

#Delete Report
@login_required(login_url='login')
def Delete_report(request, pk):
    Blotter_obj = Blotreport.objects.get(id = pk)
    Blotterall = Blotreport.objects.all()

    if Blotter_obj.Offender:
        Resident_id = Blotter_obj.Offender.id
        Resident_obj = Resident.objects.get(id = Resident_id)
        Resident_obj.Blacklisted = False
        Resident_obj.save()

        Blotter_obj.Resolved = True
        Blotter_obj.save()

        for obj in Blotterall:
            if obj.Offender == Resident_obj and obj.Resolved == False:
                Resident_obj.Blacklisted = True
                Resident_obj.save()

        messages.success(request, "Report has marked resolved")

    else:
        Blotter_obj.Resolved = True
        Blotter_obj.save()
        messages.success(request, "Report has been marked resolved")

    return redirect('/blotter_display/')

#Show Report
@login_required(login_url='login')
def Blotter_display(request):
    Blotter_obj = Blotreport.objects.filter(Resolved = False)
    Include = True
    context = {
        'Blotter_obj' : Blotter_obj,
        'Include' : Include
    }
    return render(request, "blotter/blotter_display.html", context = context)

#Show Resolved Reports
@login_required(login_url='login')
def Resolved_display(request):
    Blotter_obj = Blotreport.objects.filter(Resolved = True)
    Include = False
    context = {
        'Blotter_obj' : Blotter_obj,
        'Exclude' : Include
    }
    return render(request, "blotter/blotter_display.html", context = context)


@login_required(login_url='login')
def Blotter_details(request, pk):
    url_list = []
    Blotter_obj = Blotreport.objects.get(id = pk)
    Facts = Blotter_obj.Facts.replace('','').split(',')
    Evidence_obj = Evidences.objects.filter(Report = Blotter_obj)

    for obj in Evidence_obj:
        url_list.append(obj.images.url)

    template_path = 'blotter/blotter_details.html'
    context = {'Blotter_obj' : Blotter_obj,'url_list' : url_list,'Facts' : Facts}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #Download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    response['Content-Disposition'] = 'filename="Blotter_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




    context = {
        
    }
    return render(request,"blotter/blotter_details.html",context = context)

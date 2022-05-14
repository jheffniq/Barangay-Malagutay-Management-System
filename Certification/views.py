from genericpath import exists
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Accounts.models import Official
from django.http import HttpResponse
from Resident.models import Resident
from Blotter.models import Blotreport
from Certification.models import Certrequest, Requestarchive
from .forms import Request_form, Requeststatus
from django.contrib import messages
from datetime import datetime
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import secrets


#Display Residents
@login_required(login_url='login')
def resident_list(request):
    Resident_obj = Resident.objects.all()
    cresident = Resident.objects.filter(Blacklisted = False)
    bresident = Resident.objects.filter(Blacklisted = True)

    Resident_cleared = cresident.order_by('First_name')
    Resident_blacklisted = bresident.order_by('First_name')
    Blotter_number = []
    
    for res in Resident_blacklisted:
        resid = res.id
        blo = Blotreport.objects.filter(Offender = resid)
        bloo = blo.count()
        Blotter_number.append(bloo)

    context = {
        'Resident_obj' : Resident_obj,
        'Resident_cleared': Resident_cleared,
        'Resident_blacklisted': Resident_blacklisted,
        'Blotter_number' : Blotter_number
    }
    return render(request, "certification/barangay_clearance.html",context = context)


@login_required(login_url='login')
def resident_list02(request):
    Resident_obj = Resident.objects.all()
    cresident = Resident.objects.filter(Blacklisted = False)
    bresident = Resident.objects.filter(Blacklisted = True)

    Resident_cleared = cresident.order_by('First_name')
    Resident_blacklisted = bresident.order_by('First_name')
    Blotter_number = []
    
    for res in Resident_blacklisted:
        resid = res.id
        blo = Blotreport.objects.filter(Offender = resid)
        bloo = blo.count()
        Blotter_number.append(bloo)

    context = {
        'Resident_obj' : Resident_obj,
        'Resident_cleared': Resident_cleared,
        'Resident_blacklisted': Resident_blacklisted,
        'Blotter_number' : Blotter_number
    }
    return render(request, "certification/indigency.html",context = context)

#Date_format
def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


#View Certificate
@login_required(login_url='login')
def view_certificate(request, pk):
    Resident_obj = Resident.objects.get(id = pk)
    Officials = Official.objects.get(id=1)
    Chairman = Officials.Barangay_Chairman
    Month_Today = datetime.now().strftime('%B')
    Day_Today = custom_strftime('{S}', datetime.now())
    Year_Today = datetime.now().strftime('%Y')
    
    template_path = 'certification/Certificate1.html'
    context = {'Resident_obj': Resident_obj,
                'Chairman' : Chairman,
                'Month_Today': Month_Today,
                'Day_Today': Day_Today,
                'Year_Today' : Year_Today}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #Download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    response['Content-Disposition'] = 'filename="Barangay_Clearance.pdf"'
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



#Generate Certificate
@login_required(login_url='login')
def generate_certificate(request, pk):
    Resident_obj = Resident.objects.get(id = pk)
    Officials = Official.objects.get(id=1)
    Chairman = Officials.Barangay_Chairman
    Month_Today = datetime.now().strftime('%B')
    Day_Today = custom_strftime('{S}', datetime.now())
    Year_Today = datetime.now().strftime('%Y')
    
    template_path = 'certification/Certificate1.html'
    context = {'Resident_obj': Resident_obj,
                'Chairman' : Chairman,
                'Month_Today': Month_Today,
                'Day_Today': Day_Today,
                'Year_Today' : Year_Today}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #Download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    response['Content-Disposition'] = 'attachment; filename="Barangay_Clearance.pdf"'
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


#View Second Certificate
@login_required(login_url='login')
def view_certificate02(request, pk):
    Resident_obj = Resident.objects.get(id = pk)
    Officials = Official.objects.get(id=1)
    Chairman = Officials.Barangay_Chairman
    Month_Today = datetime.now().strftime('%B')
    Day_Today = custom_strftime('{S}', datetime.now())
    Year_Today = datetime.now().strftime('%Y')
    
    template_path = 'certification/Certificate2.html'
    context = {'Resident_obj': Resident_obj,
                'Chairman' : Chairman,
                'Month_Today': Month_Today,
                'Day_Today': Day_Today,
                'Year_Today' : Year_Today}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #Download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    response['Content-Disposition'] = 'filename="Indigency_Certificate.pdf"'
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

#Generate Second Certificate
@login_required(login_url='login')
def generate_certificate02(request, pk):
    Resident_obj = Resident.objects.get(id = pk)
    Officials = Official.objects.get(id=1)
    Chairman = Officials.Barangay_Chairman
    Month_Today = datetime.now().strftime('%B')
    Day_Today = custom_strftime('{S}', datetime.now())
    Year_Today = datetime.now().strftime('%Y')
    
    template_path = 'certification/Certificate2.html'
    context = {'Resident_obj': Resident_obj,
                'Chairman' : Chairman,
                'Month_Today': Month_Today,
                'Day_Today': Day_Today,
                'Year_Today' : Year_Today}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #Download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    response['Content-Disposition'] = 'attachment; filename="Indigency_Certificate.pdf"'
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

def request_list(request):
    form = Request_form()
    statform = Requeststatus()
    request_code = secrets.token_hex(2)
    str = " "
    while True:
        if Certrequest.objects.filter(Requestcode=request_code).exists():
            request_code = secrets.token_hex(2)
        else:
            break

    if request.method == "POST":
        form = Request_form(request.POST)
        if form.is_valid():
            CheckResident = form.save(commit = False)
            Rcode = CheckResident.Resident_code

            try:
                Resident_obj = Resident.objects.get(Resident_code = Rcode)
                if Resident_obj.Blacklisted == True:
                    messages.error(request,"Sorry, you are not eligible for a certification")
                    return redirect('/request_certificate/')
                else:
                    CheckResident.Requester = Resident_obj
                    CheckResident.Requestcode = request_code
                    CheckResident.save()
                    messages.success(request, f"Your request code is:{str}{request_code}")
                    return redirect('/request_certificate/')

            except Resident.DoesNotExist:
                messages.error(request,"Resident does not exist")
                return redirect('/request_certificate/')

    context = {
            'form' : form,
            'statform' : statform
        }
    return render(request, "certification/guest_request.html",context = context)


#def Createrequest(request, request_type, pk):
#    Resident_obj = Resident.objects.get(id = pk)
#    if request.method == "POST":
#        form = Request_form(request.POST)
#       if form.is_valid():
#            form.save()
#            request_obj = Certrequest.objects.last()
#            request_obj.Requester = Resident_obj
#           request_obj.Resident_id = pk
#            request_obj.save()

#            messages.success(request, "Request submitted for validation")
#            if request_type == 'Barangay Certificate':
#                return redirect('/request_certificate/barangay_certificate/')
#            elif request_type == 'Certificate of Indigency':
#                return redirect('/request_certificate/indigency/')

#Show Certrequests
@login_required(login_url='login')
def Renderrequest(request):
    Request_obj = Certrequest.objects.all()
    context = {
        'Request' : Request_obj
    }
    return render(request, "requests.html", context = context)

#Email cert
@login_required(login_url='login')
def Email_certificate(request, pk):
    Request_obj = Certrequest.objects.get(id=pk)
    Request_type = Request_obj.Request_type
    receiver = Request_obj.Email
    Resident_id = Request_obj.Requester.id

    Resident_obj = Resident.objects.get(id = Resident_id)

    Officials = Official.objects.get(id=1)
    Chairman = Officials.Barangay_Chairman

    Month_Today = datetime.now().strftime('%B')
    Day_Today = custom_strftime('{S}', datetime.now())
    Year_Today = datetime.now().strftime('%Y')
    
    success_message = "Certificate has been sent to the email: {}".format(receiver)

    if Request_type == "Barangay Certificate":
        template_path = 'certification/Certificate1.html'

    elif Request_type == "Certificate of Indigency":
        template_path = 'certification/Certificate2.html'
    else:
        template_path = 'certification/Certificate1.html'

    context = {'Resident_obj': Resident_obj,
                'Chairman' : Chairman,
                'Month_Today': Month_Today,
                'Day_Today': Day_Today,
                'Year_Today' : Year_Today}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #Download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    response['Content-Disposition'] = 'filename="Indigency_Certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    email = EmailMessage(
        'Barangay Malagutay Certificate Request',
        'Good Day,\n\nAttached to this email is your requested certificate. Please check if the details written in the document are correct.\n\n\nThis is an automated email, please contact the respected barangay officials/workers if you have inquiries.',
        'testbmms88@gmail.com', 
        [receiver]
    )
    email.attach('Indigency_Certificate.pdf', response.getvalue() , 'application/pdf')
    email.send()
    Requestarchive.objects.create(
        Requestcode = Request_obj.Requestcode,
        Status = "APPROVED"
    )
    Request_obj.delete()
    messages.success(request, "Certificate has been sent")
    return redirect('/display_requests/')

    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#Decline cert
@login_required(login_url='login')
def Declinerequest(request, pk):
    Request_obj = Certrequest.objects.get(id = pk)
    receiver = Request_obj.Email
    email = EmailMessage(
        'Barangay Malagutay Certificate Request',
        'Good Day,\n\nUnfortunately, your request for certificate has been declined. Please contact the barangay officials/representatives regarding this issue.\n\n\nThis is an automated email, do not reply. Please contact the respected barangay officials/workers if you have inquiries.',
        'testbmms88@gmail.com', 
        [receiver]
    )
    email.send()
    Requestarchive.objects.create(
        Requestcode = Request_obj.Requestcode,
        Status = "DENIED"
    )
    Request_obj.delete()
    messages.success(request, "Request has been declined")
    return redirect('/display_requests/')

def Checkrequest(request):
    if request.method == 'POST':
        form = Requeststatus(request.POST)
        if form.is_valid():
            Userinput = form.cleaned_data
            #CheckStatus = form.save(commit = False)
            Code = Userinput.get('Status')

            try:
                Request_obj = Certrequest.objects.get(Requestcode = Code)
                messages.info(request, "Your request status is: PENDING")
                return redirect('/request_certificate/')

            except Certrequest.DoesNotExist:
                try:
                    Archivedrequest = Requestarchive.objects.get(Requestcode = Code)
                    Status = Archivedrequest.Status
                    str = " "
                    messages.info(request,f"Your request status is:{str}{Status}")
                    return redirect('/request_certificate/')
                except Requestarchive.DoesNotExist:
                    messages.error(request,"Request does not exist")
                    return redirect('/request_certificate/')
    



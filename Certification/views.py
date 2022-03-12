from django.shortcuts import render, redirect
from django.http import HttpResponse
from Resident.models import Resident
from Blotter.models import Blotreport
from django.contrib import messages
from datetime import datetime


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def resident_list(request):
    Resident_obj = Resident.objects.all()
    Resident_cleared = Resident.objects.filter(Blacklisted = False)
    Resident_blacklisted = Resident.objects.filter(Blacklisted = True)
    context = {
        'Resident_cleared': Resident_cleared,
        'Resident_blacklisted': Resident_blacklisted
    }
    return render(request, "certification/barangay_clearance.html",context = context)

#Date_format
def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

def generate_certificate(request, pk):
    Resident_obj = Resident.objects.get(id = pk)
    Month_Today = datetime.now().strftime('%B')
    Day_Today = custom_strftime('{S}', datetime.now())
    Year_Today = datetime.now().strftime('%Y')
    
    template_path = 'certification/Certificate1.html'
    context = {'Resident_obj': Resident_obj,
                'Month_Today': Month_Today,
                'Day_Today': Day_Today,
                'Year_Today' : Year_Today}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #Download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    response['Content-Disposition'] = 'filename="report.pdf"'
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


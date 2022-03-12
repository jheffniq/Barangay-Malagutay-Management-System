from django.shortcuts import render, redirect
from Resident.models import Resident
from Blotter.models import Blotreport
from django.contrib import messages


def barangay_certificate(request):
    Resident_obj = Resident.objects.all()
    Resident_cleared = Resident.objects.filter(Blacklisted = False)
    Resident_blacklisted = Resident.objects.filter(Blacklisted = True)
    context = {
        'Resident_cleared': Resident_cleared,
        'Resident_blacklisted': Resident_blacklisted
    }
    return render(request, "certification/barangay_clearance.html",context = context)

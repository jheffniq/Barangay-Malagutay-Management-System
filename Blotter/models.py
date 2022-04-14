from django.db import models
from tabnanny import verbose
from datetime import datetime, date
from Resident.models import Resident


class Blotreport (models.Model):

    Offender = models.ForeignKey (Resident, null = True, blank=True, default = None, on_delete = models.CASCADE)
    Offender_unregistered = models.CharField(max_length=50, null=True, blank=True, verbose_name="Offender")
    Complainant = models.CharField (max_length = 50)
    Complaint = models.TextField(max_length = 1000)
    Facts = models.TextField(max_length=250)
    Unregistered = models.BooleanField(default = False)
    created_date = models.DateTimeField (auto_now_add=True)
    modified_date = models.DateTimeField (auto_now=True)

class Evidences (models.Model):
    Report = models.ForeignKey(Blotreport, null = True, blank = True, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to= "images/")

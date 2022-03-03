from django.db import models
from tabnanny import verbose
from datetime import datetime, date
from Resident.models import Resident


class Blotreport (models.Model):

    Offender = models.ForeignKey (Resident, null = True, default = None, on_delete = models.CASCADE)
    Complainant = models.CharField (max_length = 50)
    Complaint = models.TextField(max_length = 250)
    created_date = models.DateTimeField (auto_now_add=True)
    modified_date = models.DateTimeField (auto_now=True)

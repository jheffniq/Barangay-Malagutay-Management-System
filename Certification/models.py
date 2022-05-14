from django.db import models
from django.forms import IntegerField
from Resident.models import Resident

class Certrequest(models.Model):
    Requester = models.ForeignKey (Resident, null = True, default = None, on_delete = models.CASCADE)
    Resident_id = models.CharField(max_length=250)
    Resident_code = models.CharField(max_length=500, null=False, blank=False)
    Request_choices = (
        ('Barangay Certificate','Barangay Certificate'),
        ('Certificate of Indigency','Certificate of Indigency')
    )
    Request_type = models.CharField(max_length=100, choices=Request_choices, default="")
    Email = models.EmailField(max_length=254)
    Purpose = models.CharField(max_length=100)
    Requestcode = models.CharField(max_length=10)

class Requestarchive(models.Model):
    Requestcode = models.CharField(max_length=10)
    Status = models.CharField(max_length=20)
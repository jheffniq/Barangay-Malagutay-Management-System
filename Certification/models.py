from django.db import models
from django.forms import IntegerField
from Resident.models import Resident

class Certrequest(models.Model):
    Requester = models.ForeignKey (Resident, null = True, default = None, on_delete = models.CASCADE)
    Resident_id = models.CharField(max_length=250)
    Request_type = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    Purpose = models.CharField(max_length=100)
from django.db import models
from django.forms import IntegerField

class Certrequest(models.Model):
    Resident_id = models.CharField(max_length=250)
    Request_type = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    Purpose = models.CharField(max_length=100)
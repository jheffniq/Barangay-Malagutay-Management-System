from django.db import models

class Official (models.Model):
    Barangay_Chairman = models.CharField(max_length=50)
    Barangay_Secretary = models.CharField(max_length=50)
    Barangay_Treasurer = models.CharField(max_length=50)
    SK_Chairman = models.CharField(max_length=50)
 
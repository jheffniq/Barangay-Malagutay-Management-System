from django.db import models
from django.contrib.auth.models import User

class Official (models.Model):
    Barangay_Chairman = models.CharField(max_length=50)
    Barangay_Secretary = models.CharField(max_length=50)
    Barangay_Treasurer = models.CharField(max_length=50)
    Barangay_Councilors = models.TextField(max_length=500)
    SK_Chairman = models.CharField(max_length=50)
    SK_Councilors = models.TextField(max_length=500)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Position = models.CharField(max_length=250)

    def __str__(self):
        return str(self.user)
 
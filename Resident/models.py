from tabnanny import verbose
from django.db import models
from datetime import datetime, date

class Resident (models.Model):
    pic = models.ImageField(null=True, blank = True, verbose_name="Profile Picture", upload_to= "images/")
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Middle_name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Birthdate = models.DateField(auto_now_add=False, auto_now=False)
    Gender_choices = (
        ('Male','Male'),
        ('Female','Female')
        )
    Gender = models.CharField(max_length=100, choices=Gender_choices, default = "Not Specified")
    Contact = models.CharField(max_length=11)
    Citizenship = models.CharField(max_length=100) 
    Religion = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=100)
    Vac_choices = (
        ('Vaccinated','Vaccinated'),
        ('Non-Vaccinated','Non-Vaccinated')
    )
    Vaccination = models.CharField(max_length=100, choices = Vac_choices, verbose_name="Vaccination Status", default="")
    Address = models.TextField(max_length=250, verbose_name="Street Address")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.First_name} {self.Last_name}'


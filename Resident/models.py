from tabnanny import verbose
from django.db import models
from datetime import datetime, date

class Resident (models.Model):
    pic = models.ImageField(null=True, blank = True, verbose_name="Profile Picture", upload_to= "images/", default='images/default_pp.jpg')
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Middle_name = models.CharField(max_length=50)
    Birthdate = models.DateField(auto_now_add=False, auto_now=False)
    Gender_choices = (
        ('Male','Male'),
        ('Female','Female')
        )
    Gender = models.CharField(max_length=100, choices=Gender_choices, default = "Not Specified")
    Contact = models.CharField(max_length=11)
    Phealthnone = 'None'
    Phealth_choices = (
        ('None', 'None'),
        ('Employed','Employed'),
        ('Voluntary','Voluntary'),
        ('OFW','OFW'),
        ('Sponsored','Sponsored'),
        ('Indigent','Indigent'),
        ('Lifetime','Lifetime'),
        ('Senior','Senior')
    )
    Philhealth_membership = models.CharField(max_length=100,choices=Phealth_choices,default=Phealthnone,verbose_name="Philhealth Membership Type")
    Cstatus_choices = (
        ('Single','Single'),
        ('Married','Married'),
        ('Separated','Separated'),
        ('Widowed','Widowed'),
        )
    Marital_status = models.CharField(max_length=100, choices = Cstatus_choices, default = "")
    Citizenship = models.CharField(max_length=100) 
    Religion = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=100, null=True, blank=True)
    Vac_choices = (
        ('Vaccinated','Vaccinated'),
        ('Unvaccinated','Unvaccinated')
    )
    Vaccination = models.CharField(max_length=100, choices = Vac_choices, verbose_name="Vaccination Status", default="")
    Address = models.TextField(max_length=250, verbose_name="Street Address")
    Blacklisted = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.First_name} {self.Last_name}'

class CSV(models.Model):
    file_name = models.FileField(upload_to='files/csv')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    
    def __str_(self):
        return f'File id: {self.id}'

class TempResident (models.Model):
    pic = models.ImageField(null=True, blank = True, verbose_name="Profile Picture", upload_to= "images/", default='images/default_pp.jpg')
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Middle_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Birthdate = models.DateField(auto_now_add=False, auto_now=False)
    Gender_choices = (
        ('Male','Male'),
        ('Female','Female')
        )
    Gender = models.CharField(max_length=100, choices=Gender_choices, default = "Not Specified")
    Contact = models.CharField(max_length=11)
    Phealthnone = 'None'
    Phealth_choices = (
        ('None', 'None'),
        ('Employed','Employed'),
        ('Voluntary','Voluntary'),
        ('OFW','OFW'),
        ('Sponsored','Sponsored'),
        ('Indigent','Indigent'),
        ('Lifetime','Lifetime'),
        ('Senior','Senior')
    )
    Philhealth_membership = models.CharField(max_length=100,choices=Phealth_choices, default=Phealthnone,verbose_name="Philhealth Membership Type")
    Cstatus_choices = (
        ('Single','Single'),
        ('Married','Married'),
        ('Separated','Separated'),
        ('Widowed','Widowed'),
        )
    Marital_status = models.CharField(max_length=100, choices = Cstatus_choices, default = "")
    Citizenship = models.CharField(max_length=100) 
    Religion = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=100, null=True, blank=True)
    Vac_choices = (
        ('Vaccinated','Vaccinated'),
        ('Unvaccinated','Unvaccinated')
    )
    Vaccination = models.CharField(max_length=100, choices = Vac_choices, verbose_name="Vaccination Status", default="")
    Address = models.TextField(max_length=250, verbose_name="Street Address")
    Blacklisted = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.First_name} {self.Last_name}'

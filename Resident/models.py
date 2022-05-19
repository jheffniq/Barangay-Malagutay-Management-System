from tabnanny import verbose
from django.db import models
from datetime import datetime, date
from django.core.validators import RegexValidator

class Resident (models.Model):
    pic = models.ImageField(null=True, blank = True, verbose_name="Profile Picture", upload_to= "images/", default='images/default_pp.jpg')
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Middle_name = models.CharField(max_length=50, blank=True, null=True)
    Birthdate = models.DateField(auto_now_add=False, auto_now=False)
    Gender_choices = (
        ('Male','Male'),
        ('Female','Female')
        )
    Gender = models.CharField(max_length=100, choices=Gender_choices, default = "Not Specified")
    Email = models.EmailField(max_length=254, blank=True, null=True)
    numbers = RegexValidator(r'^[0-9]+','Only numbers are accepted')
    Contact = models.CharField(max_length=11, validators=[numbers])
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
    Citizenship = models.CharField(max_length=100,verbose_name="Ethnicity") 
    Religion = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=100, null=True, blank=True)
    Vac_choices = (
        ('Vaccinated','Vaccinated'),
        ('Unvaccinated','Unvaccinated')
    )
    Vaccination = models.CharField(max_length=100, choices = Vac_choices, verbose_name="Vaccination Status", default="")
    Address = models.CharField(max_length=250, verbose_name="Street Address")
    Resident_code = models.CharField(max_length=500, null=False, blank=False)
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
    identification = models.ImageField(null=False,blank=False,verbose_name="Identification Card", upload_to="images/")
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Middle_name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=254)
    Birthdate = models.DateField(auto_now_add=False, auto_now=False)
    Gender_choices = (
        ('Male','Male'),
        ('Female','Female')
        )
    Gender = models.CharField(max_length=100, choices=Gender_choices, default = "Not Specified")
    numbers = RegexValidator(r'^[0-9]+','Only numbers are accepted')
    Contact = models.CharField(max_length=11, validators=[numbers])
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
    Citizenship = models.CharField(max_length=100,verbose_name="Ethnicity") 
    Religion = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=100, null=True, blank=True)
    Vac_choices = (
        ('Vaccinated','Vaccinated'),
        ('Unvaccinated','Unvaccinated')
    )
    Vaccination = models.CharField(max_length=100, choices = Vac_choices, verbose_name="Vaccination Status", default="")
    Address = models.CharField(max_length=250, verbose_name="Street Address")
    Blacklisted = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.First_name} {self.Last_name}'
        
class Household (models.Model):
    numbers = RegexValidator(r'^[0-9]+','Only numbers are accepted')
    OwnerChoices = (('Yes','Yes'),('No','No'))
    IncomeChoices = (('131,000 and up','131,000 and up'),
                    ('41,000 - 130,000','41,000 - 130,000'),
                    ('11,000 - 40,000','11,000 - 40,000'),
                    ('Less than 10,000','Less than 10,000')
                    )

    HouseholdName = models.CharField(max_length=250)
    Head = models.ForeignKey(Resident,on_delete=models.CASCADE,verbose_name="Head of Household")
    Date = models.DateField(auto_now_add=False, auto_now=False,verbose_name="Date Established")
    Contact = models.CharField(max_length=11, validators=[numbers],verbose_name="Telephone/Mobile",null=True, blank=True)
    Address = models.CharField(max_length=500,null=True,blank=True,verbose_name="House Address")
    Homeowner = models.CharField(max_length=20,choices=OwnerChoices,default="Yes")
    Income = models.CharField(max_length=250,choices=IncomeChoices,default="")
    Member = models.ManyToManyField(Resident,related_name='mem',verbose_name="Household Members")
    Number = models.CharField(max_length=1000)

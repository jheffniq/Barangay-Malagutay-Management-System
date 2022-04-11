from django.contrib import admin
from .models import Resident, CSV, TempResident

admin.site.register(Resident)
admin.site.register(CSV)
admin.site.register(TempResident)

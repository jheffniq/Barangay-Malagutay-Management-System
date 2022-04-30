from django.contrib import admin
from .models import Blotreport, Evidences, BlotArchive

# Register your models here.
admin.site.register(Blotreport)
admin.site.register(Evidences)
admin.site.register(BlotArchive)
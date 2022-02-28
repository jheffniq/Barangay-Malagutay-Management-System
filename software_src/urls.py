"""software_src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Resident.views import Display_resident, Create_resident, Update_resident, home, Delete_resident, Display_profile

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ('home/', home),
    path('residents/', Display_resident, name = "residents"),
    path('resident_profile/<str:pk>', Display_profile, name = "resident_profile"),
    path ('resident_form/' ,Create_resident),
    path ('resident_update/<str:pk>/', Update_resident, name = "update_resident"),
    path('delete_resident/<str:pk>/', Delete_resident, name = "delete_resident"),
    path('admin/', admin.site.urls),
]

urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

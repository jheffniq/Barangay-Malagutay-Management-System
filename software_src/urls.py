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
from Accounts.views import LoginUser, LogoutUser,Guestuser
from Resident.views import Display_resident, Create_resident, Update_resident, home, Delete_resident, Display_profile, Search_resident
from Blotter.views import Addreport, Blotter_search_resident, Create_Report, Blotter_display, Blotter_details, Delete_report
from Certification.views import resident_list, generate_certificate, view_certificate
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('login/', LoginUser, name="login"),
    path('logout/', LogoutUser, name="logout"),
    path('guestuser/', Guestuser, name="guestuser"),

    path ('home/', home, name = "home"),
    path('residents/', Display_resident, name = "residents"),
    path('search_resident/', Search_resident, name = "search_resident"),
    path('resident_profile/<str:pk>/', Display_profile, name = "resident_profile"),
    path ('resident_form/' ,Create_resident),
    path ('resident_update/<str:pk>/', Update_resident, name = "update_resident"),
    path('delete_resident/<str:pk>/', Delete_resident, name = "delete_resident"),
    
    path('add_report/', Addreport, name = "add_report"),
    path('blotter_search_resident/', Blotter_search_resident, name = "blotter_search_resident"),
    path('blotter_form/<str:pk>/', Create_Report, name = "blotter_form"),
    path('blotter_display/', Blotter_display, name = "blotter_display"),
    path('blotter_details/<str:pk>/', Blotter_details, name = "blotter_details"),
    path('delete_report/<str:pk>/', Delete_report, name = "delete_report"),

    path('resident_list/',resident_list,name="resident_list"),
    path('view_certificate/<str:pk>', view_certificate, name="view_certificate"),
    path('generate_certificate/<str:pk>/',generate_certificate,name="generate_certificate"),

    path('admin/', admin.site.urls),
    
]
handler404 = 'Resident.views.view_404' 
urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

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
from django.shortcuts import redirect
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings

#Accounts app import
from Accounts.views import LoginUser, LogoutUser,Guestuser, Displayusers, Adduser, Edituser, Edit_officals
from Accounts.views import Deleteuser,Faqs

#Residents app import
from Resident.views import Display_resident, Create_resident, Update_resident, home
from Resident.views import Delete_resident, Display_profile, Search_resident, Temp_Resident, display_registrations
from Resident.views import registration_profile, Acceptresident, Declineresident

#Blotter app import
from Blotter.views import Addreport, Blotter_search_resident, Create_Report, Blotter_display
from Blotter.views import Blotter_details, Delete_report, Create_Report_unregistered

#Certification app import
from Certification.views import resident_list, resident_list02, generate_certificate, view_certificate 
from Certification.views import view_certificate02, generate_certificate02, request_list 
from Certification.views import Renderrequest, Email_certificate, Declinerequest



urlpatterns = [

    #Landing page paths
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
    path('login/', LoginUser, name="login"),
    path('logout/', LogoutUser, name="logout"),
    path('adduser/',Adduser, name = "adduser"),
    path('edit_user/', Edituser, name = "edituser"),
    path('delete_user/<str:pk>/',Deleteuser, name="deleteuser"),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name="change_password.html",success_url=reverse_lazy('users')), name = "change_password"),
    path('edit_officals/', Edit_officals, name = "edit_officials"),
    path('index/', Guestuser, name="index"),
    path('request_certificate/', request_list, name = "request_certificate"),
    #path('request_certificate/<request_type>/<str:pk>/', Createrequest, name="Createrequest"),

    #Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_complete.html"), name="password_reset_complete"),
    

    #Resident paths
    path ('home/', home, name = "home"),
    path('users/', Displayusers, name = "users"),
    path('residents/', Display_resident, name = "residents"),
    path('search_resident/', Search_resident, name = "search_resident"),
    path('resident_profile/<str:pk>/', Display_profile, name = "resident_profile"),
    path ('resident_form/' ,Create_resident),
    path ('resident_update/<str:pk>/', Update_resident, name = "update_resident"),
    path('delete_resident/<str:pk>/', Delete_resident, name = "delete_resident"),
    path('temp_resident/',Temp_Resident, name = "tempresident"),
    path ('display_registrations/', display_registrations, name = "display_registrations"),
    path ('temp_profile/<str:pk>', registration_profile, name = "temp_profile"),
    path('acceptresident/<str:pk>', Acceptresident, name = "acceptresident"),
    path('declineresident/<str:pk>', Declineresident, name= "declineresident"),
    path('faq/',Faqs,name="faq"),
    
    #Blotter paths
    path('add_report/', Addreport, name = "add_report"),
    path('blotter_search_resident/', Blotter_search_resident, name = "blotter_search_resident"),
    path('blotter_form/<str:pk>/', Create_Report, name = "blotter_form"),
    path('blotter_form_unregistered/',Create_Report_unregistered,name="blotter_form_unregistered"),
    path('blotter_display/', Blotter_display, name = "blotter_display"),
    path('blotter_details/<str:pk>/', Blotter_details, name = "blotter_details"),
    path('delete_report/<str:pk>/', Delete_report, name = "delete_report"),

    #Certificate paths
    path('resident_list/',resident_list,name="resident_list"),
    path('resident_list02/',resident_list02,name="resident_list02"),
    path('view_certificate/<str:pk>', view_certificate, name="view_certificate"),
    path('generate_certificate/<str:pk>/',generate_certificate,name="generate_certificate"),
    path('view_certificate02/<str:pk>', view_certificate02, name="view_certificate02"),
    path('generate_certificate02/<str:pk>/',generate_certificate02,name="generate_certificate02"),
    path('display_requests/',Renderrequest,name="display_requests"),

    #Email Certificate
    path('email/<str:pk>/', Email_certificate, name = "email"),
    path('declinerequest/<str:pk>/', Declinerequest, name = "declinerequest"),



    path('admin/', admin.site.urls),
    
]
handler404 = 'Resident.views.view_404' 
urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

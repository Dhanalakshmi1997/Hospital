"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:

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
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('logout', views.logout, name='logout'),

    path('DoctorRegistration',views.DoctorRegistration,name='DoctorRegistration'),
    path('PatientRegistration',views.PatientRegistration,name='PatientRegistration'),
    path('Appointment',views.Appointment,name='Appointment'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('Usermodule',views.Usermodule,name='Usermodule'),
    path('Doctormodule',views.Doctormodule,name='Doctormodule'),
    path('adminmodule',views.adminmodule,name='adminmodule'),
    path('DepartmentRegistration',views.DepartmentRegistration,name='DepartmentRegistration'),

    path('view_department',views.view_department,name='view_department'),
    path('viewappointment',views.Appointment,name='viewappointment'),
    path('editdepartment/<int:id>',views.editdepartment,name='editdepartment'),
    path('deletedepartment/<int:id>',views.deletedepartment,name='deletedepartment'),
    path('updatedepartment/<int:id>',views.updatedepartment,name='updatedepartment'),


    path('view_appointment',views.view_appointment,name='view_appointment'),
    path('viewappointment',views.Appointment,name='viewappointment'),
    path('editappointment/<int:id>',views.editappointment,name='editapppointment'),
    path('deleteappointment/<int:id>',views.deleteappointment,name='deleteappointmnent'),
    path('updateappointment/<int:id>',views.updateappointment,name='updateappointment'),

    path('adminpanel',views.adminpanel,name='adminpanel'),


    path('view_doctor',views.view_doctor,name='view_doctor'),
    path('editdoctor/<int:id>',views.editdoctor,name='editdoctor'),
    path('deletedoctor/<int:id>',views.deletedoctor,name='deletedoctor'),
    path('updatedoctor/<int:id>',views.updatedoctor,name='updatedoctor'),

    path('view_patient',views.view_patient,name='view_patient'),
    path('editpatient/<int:id>',views.editpatient,name='editpatient'),
    path('deletepatient/<int:id>',views.deletepatient,name='deletepatient'),
    path('updatepatient/<int:id>',views.updatepatient,name='updatepatient'),


]

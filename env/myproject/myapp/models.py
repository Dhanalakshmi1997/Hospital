from django.db import models

# Create your models here.
class appointment(models.Model):
    patientname=models.CharField(max_length=200)
    appointmentdate=models.CharField(max_length=200)
    symptom=models.CharField(max_length=100,null=True,blank=True)
    doctorname=models.CharField(max_length=200)
    department=models.CharField(max_length=150)
    def __str__(self):
        return self.patientname

class department(models.Model):
    departmentnumber=models.CharField(max_length=200)
    departmentname=models.CharField(max_length=200)
    doctorname=models.CharField(max_length=200)
    def __str__(self):
        return self.departmentname

class patient(models.Model):
    patientname=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    contactno=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    conformpassword=models.CharField(max_length=200)
    def __str__(self):
        return self.patientname

class doctor(models.Model):
    doctorname=models.CharField(max_length=200)
    specialation=models.CharField(max_length=200)
    gender=models.CharField(max_length=200,null=True,blank=True)
    dob=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    contactno=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    conformpassword=models.CharField(max_length=200)
    def __str__(self):
        return self.doctorname

class contact(models.Model):
    pname=models.CharField(max_length=200)
    mail=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
    def __str__(self):
        return self.pname


from django.shortcuts import render,redirect
from.forms import appointmentForm,departmentForm,patientForm,doctorForm,contactForm
from.models import appointment,department,patient,doctor,contact
from django.contrib.auth.models import User,auth


# Create your views here.

def home(request):
    return render(request,'home.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = patient.objects.get(username=username, password=password)
            if user is not None:
                print(user)
                return render(request, 'UserModule.html')
            return render(request, 'login.html')
        except:
            pass

        try:
            user = doctor.objects.get(username=username, password=password)
            if user is not None:
                print(user)
                return render(request, 'DoctorModule.html')
            return render(request, 'login.html')
        except:
            pass
    else:
        return render(request, 'login.html')


def DoctorRegistration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['conformpassword']
        if password == password1:
            if User.objects.filter(username=username).exists():
                # message.info(request,"username taken")
                return redirect('DoctorRegistration')
            user = User.objects.create_user(username=username, password=password)
            user.save()
            # print("user created")
        else:
            # print("password not matched")
            return redirect('DoctorRegistration')
        return redirect('/')
    else:
        return render(request,'DoctorRegistration.html')

def PatientRegistration(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                # message.info(request,"username taken")
                return redirect('PatientRegistration')
            user=User.objects.create_user(username=username,password=password)
            user.save()
            #print("user created")
        else:
            #print("password not matched")
            return redirect('PatientRegistration')
        return redirect('/')
    else:
        return render(request,'PatientRegistration.html')



def Appointment(request):
    if request.method=="POST":
        form=appointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=appointmentForm()
        return render(request,'appointment.html')





def about(request):
    return render(request,'about.html')

def logout(request):
    return render(request,'home.html')
def contact(request):
    if request.method=="POST":
        form=contactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=contactForm()
        return render(request,'contact.html')


def Usermodule(request):
    return render(request,'Usermodule.html')
def Doctormodule(request):
    return render(request,'Doctormodule.html')
def adminmodule(request):
    return render(request,'adminmodule.html')


def DepartmentRegistration(request):
    if request.method == "POST":
        form = departmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = departmentForm()
    return render(request, 'departmentregistration.html')

#dep list view
def view_department(request):
    result=department.objects.all()
    return render(request,'view_department.html',{'result':result})

#edit dep
def editdepartment(request,id):
    result=department.objects.get(id=id)
    return render(request,'editdepartment.html',{'result':result})

#delete dep
def deletedepartment(request,id):
    result=department.objects.get(id=id)
    result.delete()
    return redirect('/view_department')

#update dep
def updatedepartment(request,id):
    result=department.objects.get(id=id)
    form=departmentForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        return redirect('/view_department')
    return render(request,'editdepartment.html',{'result':result})


#########################################

###edit appointment
def editappointment(request,id):
    result=appointment.objects.get(id=id)
    return render(request,'editappointment.html',{'result':result})


########del appoin
def deleteappointment(request,id):
    result=appointment.objects.get(id=id)
    result.delete()
    return redirect('/view_appointment')

######update appoin
def updateappointment(request,id):
    result=appointment.objects.get(id=id)
    form=appointmentForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        return redirect('/view_appointment')
    return render(request,'editappointment.html',{'result':result})

#dep list view
def view_appointment(request):
    result=appointment.objects.all()
    return render(request,'view_appointment.html',{'result':result})



def adminpanel(request):
    return render(request,'adminpanel')

#########################################
#dep list view
def view_doctor(request):
    result=doctor.objects.all()
    return render(request,'view_doctor.html',{'result':result})

#edit dep
def editdoctor(request,id):
    result=doctor.objects.get(id=id)
    return render(request,'editdoctor.html',{'result':result})

#delete dep
def deletedoctor(request,id):
    result=doctor.objects.get(id=id)
    result.delete()
    return redirect('/view_doctor')

#update dep
def updatedoctor(request,id):
    result=doctor.objects.get(id=id)
    form=doctorForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        return redirect('/view_doctor')
    return render(request,'editdoctor.html',{'result':result})


####################################
#dep list view
def view_patient(request):
    result=patient.objects.all()
    return render(request,'view_patient.html',{'result':result})

#edit dep
def editpatient(request,id):
    result=patient.objects.get(id=id)
    return render(request,'editpatient.html',{'result':result})

#delete dep
def deletepatient(request,id):
    result=patient.objects.get(id=id)
    result.delete()
    return redirect('/view_patient')

#update dep
def updatepatient(request,id):
    result=patient.objects.get(id=id)
    form=patientForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        return redirect('/view_patient')
    return render(request,'editpatient.html',{'result':result})

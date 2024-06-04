from django import forms
from.models import appointment,department,patient,doctor,contact





class appointmentForm(forms.ModelForm):
    class Meta:
        model=appointment
        fields="__all__"
        widgets={

        }

class departmentForm(forms.ModelForm):
    class Meta:
        model=department
        fields="__all__"
        widgets={

        }

class patientForm(forms.ModelForm):
    class Meta:
        model=patient
        fields="__all__"
        widgets={

        }

class doctorForm(forms.ModelForm):
    class Meta:
        model=doctor
        fields="__all__"
        widgets={

        }

class contactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields="__all__"
        widgets={

        }
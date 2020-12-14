from django.forms import ModelForm, Textarea
from .models import doctor_review, hospital_review, doctor, doctoredu, hospital, doctoruni

class DoctorReviewForm(ModelForm):
    class Meta:
        model = doctor_review
        fields = ['rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 128, 'rows': 3})
        }

class HospitalReviewForm(ModelForm):
    class Meta:
        model = hospital_review
        fields = ['rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 128, 'rows': 3})
        }


from django import forms
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))



class EnlistDoctorForm(ModelForm):
    class Meta:
        model = doctor
        fields = ['first_name', 'last_name', 'edu', 'speciality', 'hospital', 'desc', 'profile']

class EnlistHospitalForm(ModelForm):
    class Meta:
        model = hospital
        fields = ['name', 'desc', 'building', 'street', 'city', 'pincode', 'beds','profile']

class AddDegreeForm(ModelForm):
    class Meta:
        model = doctoredu
        fields = ['degree', 'uni']

class AddUniForm(ModelForm):
    class Meta:
        model = doctoruni
        fields = ['name']
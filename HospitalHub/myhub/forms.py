from django.forms import ModelForm, Textarea
from .models import doctor_review, hospital_review

class DoctorReviewForm(ModelForm):
    class Meta:
        model = doctor_review
        fields = ['rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }

class HospitalReviewForm(ModelForm):
    class Meta:
        model = hospital_review
        fields = ['rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }
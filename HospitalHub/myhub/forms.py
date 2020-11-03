from django.forms import ModelForm, Textarea
from .models import review

class ReviewForm(ModelForm):
    class Meta:
        model = review
        fields = ['rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }
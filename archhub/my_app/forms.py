from django import forms
from .models import Hours

class HoursForm(forms.ModelForm):
    class Meta:
        model = Hours
        fields = ['day', 'open', 'close']
        widgets = {
            # 'day': forms.Select(choices=Hours.DAYS),
            'open': forms.TimeInput(attrs={'type': 'time'}),
            'close': forms.TimeInput(attrs={'type': 'time'}),
        }
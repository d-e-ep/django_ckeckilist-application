from django import forms
from .models import user

class CandidatesEnrollment(forms.ModelForm):
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'email','mobile_no' ,'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'mobile_no': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
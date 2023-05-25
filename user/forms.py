from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = (
            'employee_id',
            'investment_report',
            'training',
            'evaluation',
            'groups',
            'user_permissions'
        )

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

from django import forms
from accounts.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    password = forms.CharField(widget=forms.PasswordInput)


from django import forms
from biblioteka.models import delete


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = delete
        fields = ['nomer']

class new_book(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)
    opisanie = forms.CharField(max_length=10000)
    date = forms.DateField()


class izmenen(forms.Form):
    id_book = forms.CharField(max_length=10)
    element = forms.CharField(max_length=10)
    na_cho = forms.CharField(max_length=10000)
from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()

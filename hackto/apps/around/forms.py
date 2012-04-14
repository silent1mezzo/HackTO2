from django import forms
from django.contrib.localflavor.ca.forms import CAPostalCodeField

class SearchForm(forms.Form):
    forms.CharField(widget=forms.TextInput(attrs={'class':'input-xxlarge', 'placeholder':'Enter your address/postal code...'}))

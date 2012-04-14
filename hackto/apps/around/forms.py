from django import forms
from django.contrib.localflavor.ca.forms import CAPostalCodeField

class SearchForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'input-xxlarge', 'placeholder':'Enter your address..self.'}))
    postal_code = CAPostalCodeField(required=False, widget=forms.TextInput(attrs={'class':'input-small', 'placeholder':'Postal Code...'}))

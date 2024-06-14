from django import forms
from .models import *

class travelgramForm(forms.ModelForm):
    class Meta:
        model=Travelgram
        fields='__all__'

__author__ = 'joaquin'
from models import FSUser
from django.forms import ModelForm
from django.forms import forms

import csv

class CarregaUsuaris(ModelForm):
    file_to_import = forms.FileField()
    class Meta:
        model = FSUser
        fields = ("file_to_import", "place")





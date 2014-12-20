__author__ = 'joaquin'
from models import FSUser
from django.forms import ModelForm
from django.forms import forms

import csv

class CarregaUsuaris(forms.Form):
    file = forms.FileField()
    def save(self):
        records = csv.reader(self.cleaned_data["file"])
        for line in records:
            input_data = Data()
            input_data.place = self.cleaned_data["place"]
            input_data.time = datetime.strptime(line[1], "%m/%d/%y %H:%M:%S")
            input_data.data_1 = line[2]
            input_data.data_2 = line[3]
            input_data.data_3 = line[4]
            input_data.save()





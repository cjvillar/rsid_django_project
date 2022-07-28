from dataclasses import field
from xml.dom import ValidationErr
from django import forms
from .models import Rsids
from django.core.exceptions import ValidationError
import re

class RsidsForm(forms.ModelForm):
    class Meta:
        model = Rsids
        fields = ['rs_id','gene','diseases']
        widgets = {
            'rs_id': forms.TextInput(attrs={'class': 'form-control '}),
            'gene': forms.Textarea(attrs={'class': 'form-control '}),
            'diseases': forms.Textarea(attrs={'class': 'form-control'}),
        }
        # labels = {
        #     'rs_id': "Put rsID here:"
        # }

    def clean_rsid(self):
        rs_id = self.cleaned_data['rs_id']
        if rs_id.startswith('rs'):
             return rs_id
        raise ValidationError('rsID must begin with "rs"')
       

    # def clean_diseases(self):
    #     disease = self.cleaned_data['diseases']
    #     if disease != type(dict):
    #         raise ValidationError('Disease must be a dictionary')
    #     return disease
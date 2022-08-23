import re
from dataclasses import field
from xml.dom import ValidationErr

from django import forms
from django.core.exceptions import ValidationError

from .models import Rsids


class RsidsForm(forms.ModelForm):
    class Meta:
        model = Rsids
        fields = ["rs_id", "gene", "diseases"]
        widgets = {
            "rs_id": forms.TextInput(attrs={"class": "form-control "}),
            "gene": forms.Textarea(attrs={"class": "form-control "}),
            "diseases": forms.Textarea(attrs={"class": "form-control"}),
        }
     
    def clean_rsid(self):
        rs_id = self.cleaned_data["rs_id"]
        if rs_id.startswith("rs"):
            return rs_id
        raise ValidationError('rsID must begin with "rs"')

class UploadFileForm(forms.Form):
    file = forms.FileField()

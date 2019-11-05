from django import forms
from .models import UploadFile


class SingleUploadModelForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['file']

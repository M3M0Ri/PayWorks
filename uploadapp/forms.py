from django import forms
from .models import Uploads


class UploadFrom(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = '__all__'

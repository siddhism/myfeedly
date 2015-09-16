from django import forms
from .models import *

class RssUrlForm(forms.ModelForm):
    class Meta:
        model = RssUrl
        fields = '__all__'   
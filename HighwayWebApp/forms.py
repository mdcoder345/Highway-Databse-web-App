from django import forms
from . import models

class HighwayForms(forms.ModelForm):
    class Meta:
        model=models.Highway
        fields="__all__"

class TednerForms(forms.ModelForm):
    class Meta:
        model=models.Tender
        fields="__all__"
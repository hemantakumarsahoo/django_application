from django import forms
from .models import App

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['name', 'icon', 'app_link', 'category', 'sub_category', 'points']

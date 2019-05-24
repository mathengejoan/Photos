from django import forms
from .models import Images
from django.contrib.auth.models import User


class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['name', 'cover', 'year']



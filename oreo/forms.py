from django import forms
from .models import Album, Images
from django.contrib.auth.models import User


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'cover', 'year']



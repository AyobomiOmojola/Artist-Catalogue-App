from django import forms
from . import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__'

class AlbulmForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type' : 'date'}))
    class Meta:
        model = models.Albulm
        fields = '__all__'

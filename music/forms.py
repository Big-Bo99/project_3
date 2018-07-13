from django import forms

from .models import Download

class Form(forms.ModelForm):

    class Meta:
        model = Download
        fields = ('youtube_link', 'email')

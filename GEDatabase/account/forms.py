from django import forms
from django.contrib.auth.models import User
from .models import Profile, Instrument

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class LendInstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ('name','brand','serial')
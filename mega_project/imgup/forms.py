from django import forms
from django.db import models


class ImageForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    

class LoginForm(forms.Form):
    name = forms.CharField(max_length=32, label = 'Name',initial='Your name goes here')
    password = forms.CharField(max_length=32, label='password' ,widget=forms.PasswordInput,initial='Pass')
    
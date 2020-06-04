from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from . import models


class UserForm(ModelForm):
    password = forms.CharField(
        max_length=6,
        widget=forms.PasswordInput(),
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserInfoForm(ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['facebook_link', 'profile_pic']
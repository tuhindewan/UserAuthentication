from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    dictionary = {

    }
    return render(request, 'ua/index.html', context=dictionary)

def registration(request):
    userForm = forms.UserForm()
    userInfoForm = forms.UserInfoForm()
    dictionary = {
        'userForm': userForm,
        'userInfoForm': userInfoForm,
    }
    return render(request, 'ua/registration.html', context=dictionary)   
from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    dictionary = {

    }
    return render(request, 'ua/index.html', context=dictionary)

def registration(request):
    userForm = forms.UserForm()
    userInfoForm = forms.UserInfoForm()
    registered = False
    
    if request.method == 'POST':
        userFormData = forms.UserForm(data=request.POST)
        userInfoFormData = forms.UserInfoForm(data=request.POST)

        if userFormData.is_valid() and userInfoFormData.is_valid():
            user = userFormData.save()
            user.set_password(user.password)
            user.save()

            user_info = userInfoFormData.save(commit=False)
            user_info.user = user

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']

            user_info.save()
            registered = True    
    # else:
    #     userForm = forms.UserForm()
    #     userInfoForm = forms.UserInfoForm()

    dictionary = {
        'userForm': userForm,
        'userInfoForm': userInfoForm,
        'registered': registered,
    }
    return render(request, 'ua/registration.html', context=dictionary)


def login_page(request):
    dictionary = {

    }   
    return render(request, 'ua/login.html', context=dictionary)   


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('UA:UA_index'))
            return HttpResponse('Your Account is Inactive!!')
        else:
            return HttpResponse("Invalid Credentials!!")        
    
    return HttpResponseRedirect(reverse('UA:ua_login'))

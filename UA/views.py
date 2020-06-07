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
from django.shortcuts import render

# Create your views here.

def index(request):
    dictionary = {

    }
    return render(request, 'ua/index.html', context=dictionary)

def registration(request):
     dictionary = {

     }
     return render(request, 'ua/registration.html', context=dictionary)   
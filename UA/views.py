from django.shortcuts import render

# Create your views here.

def index(request):
    dictionary = {

    }
    return render(request, 'ua/index.html', context=dictionary)
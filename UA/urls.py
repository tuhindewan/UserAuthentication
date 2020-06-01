from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'UA'

urlpatterns = [
    path('', views.index, name='UA_index'),
]

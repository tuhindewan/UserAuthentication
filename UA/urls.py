from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'UA'

urlpatterns = [
    path('', views.index, name='UA_index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_page, name='ua_login'),
]

# Backend\Students\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('Login/', views.login, name='login'),
    path('Registration/', views.registration, name='registration'),
]

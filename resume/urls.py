"""Схема URL для resume"""
from django.urls import path, include
from . import views

app_name = 'resume'
urlpatterns = [
    # домашняя страница
    path('resume/', views.resume, name='resume'),
]
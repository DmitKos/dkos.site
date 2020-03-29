"""Схема URL для blog"""
from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    # домашняя страница
    path('', views.index, name='index'),
]
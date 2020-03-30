"""Схема URL для blog"""
from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    # домашняя страница
    path('', views.index, name='index'),
    # страница блога со списком постов (Topic)
    path('blog/', views.topics, name='topics'),
    # страница для каждого поста (Topic)
    path('topics/<str:slug>/', views.topic, name='topic'),
]
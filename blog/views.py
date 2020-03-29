from django.shortcuts import render

# Create your views here.
def index(request):
    """Домашняя страница приложения blog"""
    return render(request, 'blog/index.html')
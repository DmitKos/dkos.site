from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """Logout"""
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))

def register(request):
    """Представление страницы регистрации нового пользователя"""
    if request.method != 'POST':
        # Пустая форма
        form = UserCreationForm()
    else:
        # Обработка заполненной формы
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Вход и редирект на домашнюю страницу
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('blog:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

from django.shortcuts import render
from users.forms import LoginForm, RegisterForm

def login(request):
    form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def register(request):
    form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})
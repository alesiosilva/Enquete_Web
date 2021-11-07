from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView


# Create your views here.

def login(request):
    login = LoginView()
    return render(request, login)

def register(request):
    return render(request, 'user/register.html')
    
def logout(request):
    return render(request, 'user/logout.html')
    
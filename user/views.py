from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.views import LoginView
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.conf import settings

# Create your views here.

def login(request):
    login = LoginView()
    return render(request, login)

# View para cadastro de usuários no django
def register(request):
    template_name = 'user/register.html' 
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)
    context = {'form': form}
    return render(request, template_name, context)
    
def logout(request):
    return render(request, 'user/logout.html')
    
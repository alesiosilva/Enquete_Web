from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, get_object_or_404
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.conf import settings

# Create your views here.

# View para cadastro de usuários no django
def register(request):
    template_name = 'user/register.html' 
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()

        # Login automático após cadastro
        user = authenticate(
            username = user.username,
            password = form.cleaned_data['password1'],
        )
        login(request, user)
        # Retorno para index após cadastro
        return redirect('curso:index')
        
        # Retorno para tela de URL após cadastro
        # return redirect(settings.LOGIN_URL)
    context = {'form': form}
    return render(request, template_name, context)

# View para painel do usuário com requisição de login
# Redireciona ao login automaticamente caso não esteja logado
@login_required    
def dashboard(request):
    template_name = 'user/dashboard.html'
    return render(request, template_name)

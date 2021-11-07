from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect

from .models import *
from .forms import *

# Create your views here.

def courses(request):
    cursos = Course.objects.all()
    template = 'curso/index.html'
    return render(request, template, {'cursos': cursos})

def detail(request, slug):
    curso = get_object_or_404(Course, slug=slug)
    return render(request, 'curso/detail.html', {'curso': curso})

# Nova view de contato com form e envio de email separados
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        course = Course.objects.get(pk=request.POST['course'])
        form.send_mail(course)
        form.save()
        form = ContactForm()
        alert = 'Obrigado, recebemos sua mensagem com sucesso!'
        context = {
            'form': form,
            'alert': alert,
        }
        return render(request, 'curso/contact.html', context)
    return render(request, 'curso/contact.html', {'form': form})
        
    

''' Antigo contato com envio de e-mail integrado a view
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        course = Course.objects.get(pk=request.POST['course'])
        form.save()
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        msg = form.cleaned_data['msg']
        subject = 'Contato sobre o curso: ' + course.name
        message = 'Olá prezado, %(name)s\nRecebemos sua solicitação através do nosso formulário Django: \nE-mail: %(email)s\nMensagem: %(msg)s \nData: %(date)s'
        context = {'course': course.name, 'name': name, 'email': email, 'msg': msg,}
        message = message % context
        alert = 'Obrigado, recebemos sua mensagem com sucesso!'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
        return render(request, 'curso/contact.html', {'form': form, 'alert': alert})
    return render(request, 'curso/contact.html', {'form': form})
'''
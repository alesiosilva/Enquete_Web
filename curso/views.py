from django.conf import settings
from django.core.mail import send_mail
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, render, redirect

from .models import *

# Create your views here.

def courses(request):
    cursos = Course.objects.all()
    template = 'curso/index.html'
    return render(request, template, {'cursos': cursos})

def detail(request, slug):
    curso = get_object_or_404(Course, slug=slug)
    return render(request, 'curso/detail.html', {'curso': curso})

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

def contact(request):
    contato = ContactForm(request.POST or None)
    course = Course.objects.get(pk=request.POST['course'])
    if contato.is_valid():
        contato.save()
        name = contato.cleaned_data['name']
        email = contato.cleaned_data['email']
        msg = contato.cleaned_data['msg']
        date = contato.cleaned_data['date']
        subject = 'Contato sobre o curso: ' + course.name
        message = 'Olá prezado, %(name)s\nRecebemos sua solicitação através do nosso formulário Django: \nE-mail: %(email)s\nMensagem: %(msg)s \nData: %(date)s'
        context = {'name': name, 'email': email, 'msg': msg, 'date': date,}
        message = message % context
        alert = 'Obrigado, recebemos sua mensagem com sucesso!'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
        return render(request, 'curso/contact.html', {'contato': contato, 'alert': alert})
    return render(request, 'curso/contact.html', {'contato': contato})

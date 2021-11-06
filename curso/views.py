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
    if contato.is_valid():
        contato.save()
        return redirect('curso:index')
    return render(request, 'curso/contact.html', {'contato': contato})

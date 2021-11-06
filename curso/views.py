from django.shortcuts import get_object_or_404, render

from .models import *

# Create your views here.

def courses(request):
    cursos = Course.objects.all()
    template = 'curso/index.html'
    return render(request, template, {'cursos': cursos})

def detail(request, slug):
    curso = get_object_or_404(Course, slug=slug)
    return render(request, 'curso/detail.html', {'curso': curso})
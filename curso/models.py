from django.db import models
from django.db.models.base import Model
from django.utils import timezone

# Create your models here.
class Course(models.Model):
    name = models.CharField('Curso', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data Início', null=True, blank=True)
    created_date = models.DateTimeField('Criado', default=timezone.now)
    updated_date = models.DateTimeField('Atualizado', auto_now=True)
    image = models.ImageField(upload_to='curso_images', verbose_name='Imagem', blank=True, null=True)
    duration = models.DurationField('Carga horária', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

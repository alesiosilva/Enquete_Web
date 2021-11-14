from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.conf import settings

# Modelagem de dados para regra de negócio.
# Model para cadastro de cursos
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

# Model para cadastro de inscrições entre usuários e cursos
class Enrollment(models.Model):

    STATUS_CHOICES = (
        (0, 'Pendente'), 
        (1, 'Ativo'), 
        (2, 'Cancelado')
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuário', 
        related_name='enrollments', 
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course, 
        verbose_name='Curso', 
        related_name='enrollments',
        on_delete=models.CASCADE
    )
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=1, blank=True)
    created_at = models.DateTimeField('Inscrito em', default=timezone.now)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def active(self):
        self.status = 1
        self.save()

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        # atributo para relacionar uma única inscrição para cada usuário no model sem duplicidades.
        unique_together = (('user', 'course'))


# Model para registro de contatos relacionado a algum curso
class Contact(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(null=True)
    msg = models.TextField()
    date = models.DateTimeField('data contato', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contato'

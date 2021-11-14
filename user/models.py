from io import RawIOBase
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.deletion import CASCADE

# Model customizado para recuperação de senha
'''
class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, verbose_name='Usuário')
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()'''

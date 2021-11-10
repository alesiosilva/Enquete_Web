from io import RawIOBase
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.deletion import CASCADE

# Model customizado para recuperação de senha

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, verbose_name='Usuário')


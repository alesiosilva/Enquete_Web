from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Formulário para cadastro do usuário
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    #birthdate = forms.DateField(label='Data de nascimento')

    # Função para validar email já cadastrado
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail já cadastrado, favor preencher um novo email.')
        return email

    # Função herdada de UserCreationForm para cadastros de novos campos do user
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        if commit:
            user.save()
        return user
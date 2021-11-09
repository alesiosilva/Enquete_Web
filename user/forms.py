from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
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

# Formulário para alteração do cadastro de usuário
class EditUserForm(forms.ModelForm):
    # Função para validar email já cadastrado
    def clean_email(self):
        email = self.cleaned_data['email']
        query_set = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if query_set.exists():
            raise forms.ValidationError('E-mail já cadastrado, favor preencher um novo email.')
        return email
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']



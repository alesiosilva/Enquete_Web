from django.forms import ModelForm
from .models import *
from django.core.mail import send_mail
from djangosite.mail import send_mail_template


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('course', 'name', 'email', 'phone', 'msg')

    def send_mail(self, course):
        subject = 'Contato sobre o curso: ' + course.name
        context = {
            'course': course.name,
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'phone': self.cleaned_data['phone'],
            'msg': self.cleaned_data['msg'],
        }
        template_name = 'curso/contact_email.html'
        send_mail_template(subject, template_name, context, [context['email']])
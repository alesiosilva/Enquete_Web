from django import conf
from django.template import Library
from curso.models import Enrollment

register = Library()

@register.inclusion_tag('curso/my_courses.html')
def my_courses(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context


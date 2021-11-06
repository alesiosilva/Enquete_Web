from django.contrib import admin
from django.db.models import fields
from .models import *
# Register your models here.

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # Adicionando campos da escolha
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # Adicionando escolhas em linhas
    inlines = [ChoiceInline]

    # Adicionando colunas na administração de escolhas
    list_display = ('question_text', 'pub_date')


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)

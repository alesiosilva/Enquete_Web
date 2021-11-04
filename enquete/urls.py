from os import name
from django.urls import path
from . import views

# Namespace da aplicação
app_name = 'enquete'
urlpatterns = [
    path('', views.index, name='index'),
    # Substituindo views.<name_template> --> views.NameView.as_view()
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('contato/', views.contact, name='contact')
]
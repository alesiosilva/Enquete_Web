from django.urls import path
from . import views

app_name = 'curso'
urlpatterns = [
    path('', views.courses, name='index'),
    path('detail/<slug:slug>', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),

]
from django.urls import path
from curso import views

app_name = 'curso'
urlpatterns = [
    path('', views.courses, name='index'),
    path('detail/<slug:slug>', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('enrollment/<slug:slug>', views.enrollment, name='enrollment'),

]
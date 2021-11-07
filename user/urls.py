from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'curso:index'), name='logout'),

]
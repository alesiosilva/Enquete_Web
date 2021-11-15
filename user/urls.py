from django.urls import path, base
from django.urls.conf import include
from user import views
from django.contrib.auth import views as auth_views

app_name = 'user'
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='curso:index'), name='logout'),
    path('panel/', views.panel, name='panel'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('edit_password/', views.edit_password, name='edit_password'),
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='user/reset.html',
        email_template_name='user/reset_email.html',
        success_url=base.reverse_lazy('user:password_reset_done')), name='password_reset'),
    path('reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='user/reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='user/reset_confirm.html', 
        success_url=base.reverse_lazy('user:password_reset_complete')), name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='user/reset_complete.html'), name='password_reset_complete'),
]
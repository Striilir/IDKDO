from django.urls import path

from django.contrib.auth import views as coco

from .forms import LoginForm

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', coco.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user='true', authentication_form=LoginForm), name='login'),
    path('logout/', coco.LogoutView.as_view(template_name='accounts/logout.html', next_page='accounts:login'), name='logout'),

]

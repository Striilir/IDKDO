from django.contrib import admin
from django.urls import path, include

from app.View.loginView import LoginFormView
from gift.views import frontpage , idea_detail, idea_creation
urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('login/', LoginFormView.as_view(), name='login'),
    path('new/', idea_creation, name='idea_creation'),
    path('<slug:slug>/', idea_detail, name='idea_detail'),
    path('accounts/', include('accounts.urls')),


]

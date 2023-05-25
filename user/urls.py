from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.home, name='home'),
    path('register_user/', views.register_view, name='register_user'),
    path('login/', views.login_view, name='login'),
]

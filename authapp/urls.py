from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_staff, name='login'),
    path('register', views.register_staff, name='register'),
]

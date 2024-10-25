from django.urls import path
from . import views

urlpatterns = [
    path('sistema_login', views.sistema_login, name='sistema_login'),
]

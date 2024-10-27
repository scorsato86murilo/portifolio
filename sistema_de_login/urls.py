from django.urls import path
from . import views

urlpatterns = [
    path('sistema_login', views.sistema_login, name='sistema_login'),
    path('sistema_login_entrar', views.sistema_login_entrar, name='sistema_login_entrar'),
    path('sistema_login_plataforma', views.sistema_login_plataforma, name='sistema_login_plataforma'),
    path('recuperar_senha', views.enviar_email, name='enviar_email'),
]

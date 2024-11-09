from django.urls import path
from . import views

urlpatterns = [
    path('gestao_salario_cadastro/', views.gestao_salario_cadastro, name='gestao_salario_cadastro'),
    path('gestao_salario_entrar/', views.gestao_salario_entrar, name='gestao_salario_entrar'),
    path('gestao_salario_painel/', views.gestao_salario_painel, name='gestao_salario_painel'),
    path('logout_view_sair', views.logout_view_sair, name='logout_view_sair'),

]


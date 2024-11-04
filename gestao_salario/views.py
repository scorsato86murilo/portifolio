from django.shortcuts import render


def gestao_salario_cadastro(request):
    if request.method == 'GET':
        return render(request, 'gestao_salario_cadastro.html')
    if request.method == 'POST':
        return render(request, 'gestao_salario_cadastro.html')


def gestao_salario_entrar(request):
    if request.method == 'GET':
        return render(request, 'gestao_salario_entrar.html')
    if request.method == 'POST':
        return render(request, 'gestao_salario_entrar.html')


def gestao_salario_painel(request):
    if request.method == 'GET':
        return render(request, 'gestao_salario_painel.html')
    if request.method == 'POST':
        return render(request, 'gestao_salario_painel.html')
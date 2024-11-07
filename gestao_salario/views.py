from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from gestao_salario.models import Salario


def gestao_salario_cadastro(request):
    if request.method == 'GET':
        return render(request, 'gestao_salario_cadastro.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Verificar se as senhas coincidem
        if password2 != password:
            messages.error(request, 'As senhas são diferentes!')
            return render(request, 'gestao_salario_cadastro.html')

        # Verificar se todos os campos foram preenchidos
        if not username or not password:
            messages.error(request, 'Preencha todos os campos!')
            return render(request, 'gestao_salario_cadastro.html')

        # Verificar se o username já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe!')
            return render(request, 'gestao_salario_cadastro.html')

        try:
            # Criar o usuário se as verificações passarem
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('gestao_salario_entrar')
        except Exception as e:
            messages.error(request, 'Erro ao criar o usuário. Tente novamente.')
            print("Erro ao criar usuário:", e)

            return render(request, 'gestao_salario_cadastro.html')


def gestao_salario_entrar(request):
    if request.method == 'GET':
        return render(request, 'gestao_salario_entrar.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autentica o usuário
        user = authenticate(username=username, password=password)

        if user:
            # Se a autenticação foi bem-sucedida, faz login do usuário
            login(request, user)
            return redirect('gestao_salario_painel')  # Redireciona para a plataforma após login
        else:
            # Se a autenticação falhar, retorna à página de cadastro ou exibe uma mensagem de erro
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente ou cadastre-se.')
            return redirect('gestao_salario_entrar')


@login_required
def gestao_salario_painel(request):
    nome = request.user

    if request.method == 'POST':
        salario_valor = request.POST.get('salario')

        if salario_valor:
            # Cria uma nova instância de Salario associada ao usuário logado
            salario = Salario(usuario=request.user, salario=float(salario_valor))
            salario.save()

    # Pega o último salário do usuário logado (independente de GET ou POST)
    ultimo_salario = Salario.objects.filter(usuario=request.user).order_by('-id').first()

    # Renderiza a página com os dados
    return render(request, 'gestao_salario_painel.html', {
        'nome': nome,
        'ultimo_salario': ultimo_salario  # Passa o último salário para o template
    })


def logout_view_sair(request):
    logout(request)
    # Redirecione para onde você deseja após o logout
    return redirect('gestao_salario_entrar')

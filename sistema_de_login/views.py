import random
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback


def sistema_login(request):
    if request.method == 'GET':
        return render(request, 'index_sistema_login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('senha')
        password2 = request.POST.get('senha2')
        email = request.POST.get('email')

        # Verificar se as senhas coincidem
        if password2 != password:
            messages.error(request, 'As senhas são diferentes!')
            return render(request, 'index_sistema_login.html')

        # Verificar se todos os campos foram preenchidos
        if not username or not password or not email:
            messages.error(request, 'Preencha todos os campos!')
            return render(request, 'index_sistema_login.html')

        # Verificar se o email já existe
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado!')
            return render(request, 'index_sistema_login.html')

        # Verificar se o username já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe!')
            return render(request, 'index_sistema_login.html')

        try:
            # Criar o usuário se as verificações passarem
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('sistema_login_entrar')
        except Exception as e:
            messages.error(request, 'Erro ao criar o usuário. Tente novamente.')
            print("Erro ao criar usuário:", e)
            print(traceback.format_exc())
            return render(request, 'index_sistema_login.html')


def sistema_login_entrar(request):
    if request.method == 'GET':
        return render(request, 'sistema_login_entrar.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('senha')

        # Autentica o usuário
        user = authenticate(username=username, password=password)

        if user is not None:
            # Se a autenticação foi bem-sucedida, faz login do usuário
            login(request, user)
            return redirect('sistema_login_plataforma')
        else:
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente ou cadastre-se.')
            return redirect('sistema_login')


def sistema_login_plataforma(request):
    if request.method == 'GET':
        return render(request, 'sistema_login_plataforma.html')
    if request.method == 'POST':
        return render(request, 'sistema_login_plataforma.html')


def enviar_email(request):
    if request.method == 'GET':
        return render(request, 'recuperar_senha.html')

    if request.method == 'POST':
        email_ = request.POST.get('email_recuperar').strip()

        # Obter o modelo de usuário
        User = get_user_model()
        try:
            user = User.objects.get(email=email_)
            if not email_:
                messages.success(request, 'Voce tem que preencher o campo Email')
                return render(request, 'recuperar_senha.html')
            else:
                messages.success(request, 'Email enviado com SUCESSO!')
        except User.DoesNotExist:
            messages.warning(request, 'Email não encontrado em nossas bases de dados!')
            return render(request, 'recuperar_senha.html')
        except Exception as e:
            messages.error(request, 'Ocorreu um erro inesperado.')
            print("Erro ao buscar usuário:", e)
            print(traceback.format_exc())
            return render(request, 'recuperar_senha.html')

        # Geração de nova senha
        nova_senha = str(random.randint(1000000, 9999999))
        user.set_password(nova_senha)
        user.save()

        # Envio de email com a nova senha
        assunto = "Recuperação de senha"
        corpo = f"Sua nova senha é: {nova_senha}. Lembre-se de alterá-la o quanto antes."
        remetente = 'gramline.recuperacao.de.senha@gmail.com'  # Substitua pelo seu email
        senha_remetente = 'eibrutfknhhwjxbi'  # Substitua pela senha do app

        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = email_
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo, 'html'))

        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(remetente, senha_remetente)
            s.sendmail(remetente, email_, msg.as_string())
            s.quit()
            messages.success(request, 'Nova senha enviada para o email.')
        except smtplib.SMTPException as e:
            messages.error(request, 'Erro ao enviar email. Tente novamente.')
            print("Erro ao enviar email:", e)
            print(traceback.format_exc())

        return render(request, 'recuperar_senha.html')


def logout_view(request):
    logout(request)
    # Redirecione para onde você deseja após o logout
    return redirect('sistema_login_entrar')

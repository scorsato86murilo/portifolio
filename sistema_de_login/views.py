from django.shortcuts import render


def sistema_login(request):

    if request.method == 'GET':
        return render(request, 'index_sistema_login.html')

    elif request.method == 'POST':
        return render(request, 'index_sistema_login.html')


def sistema_login_entrar(request):
    if request.method == 'GET':
        return render(request, 'sistema_login_entrar.html')

    elif request.method == 'POST':
        return render(request, 'sistema_login_entrar.html')


def sistema_login_plataforma(request):
    if request.method == 'GET':
        return render(request, 'sistema_login_plataforma.html')

    elif request.method == 'POST':
        return render(request, 'sistema_login_plataforma.html')

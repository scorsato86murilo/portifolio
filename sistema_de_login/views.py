from django.shortcuts import render


def sistema_login(request):

    if request.method == 'GET':
        return render(request, 'index_sistema_login.html')

    elif request.method == 'POST':
        return render(request, 'index_sistema_login.html')

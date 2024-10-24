from django.shortcuts import render

from index.models import LadoDireito


def index(request):
    if request.method == 'GET':
        lado_direito = LadoDireito.objects.first()  # Isso retorna o primeiro registro
        return render(request, 'index.html', {'lado_direito': lado_direito})

    elif request.method == 'POST':
        return render(request, 'index.html')  # Ou redirecione para outra página

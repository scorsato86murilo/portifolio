from django.shortcuts import render

from index.models import LadoDireito, VideoApresentacao


def index(request):
    if request.method == 'GET':
        lado_direito = LadoDireito.objects.first()  # Retorna o primeiro registro de LadoDireito
        video = VideoApresentacao.objects.first()  # Retorna o primeiro registro de VideoApresentacao

        return render(request, 'index.html', {'lado_direito': lado_direito,
                                              'video': video,
                                              })
    elif request.method == 'POST':
        return render(request, 'index.html')  # Ou redirecione para outra página


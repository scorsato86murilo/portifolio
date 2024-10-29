from django.shortcuts import render

from index.models import LadoDireito, VideoApresentacao, Projeto


def index(request):
    if request.method == 'GET':
        lado_direito = LadoDireito.objects.first()  # Retorna o primeiro registro de LadoDireito
        video = VideoApresentacao.objects.first()  # Retorna o primeiro registro de VideoApresentacao

        projetos = Projeto.objects.all()

        return render(request, 'index.html', {'lado_direito': lado_direito,
                                              'video': video,
                                              'projetos': projetos,

                                              })
    elif request.method == 'POST':
        return render(request, 'index.html')  # Ou redirecione para outra página


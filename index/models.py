from django.db import models


class LadoDireito(models.Model):
    foto = models.ImageField(upload_to='img_Direito')
    zap = models.CharField(max_length=30)
    instagram = models.CharField(max_length=70)
    youtube = models.CharField(max_length=70)
    linkedin = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    texto = models.TextField()

    def __str__(self):
        return 'Editar Lado Direito'


class VideoApresentacao(models.Model):
    video = models.CharField(max_length=100)

    def __str__(self):
        return self.video


class Projeto(models.Model):
    ordem = models.IntegerField()
    img_projeto = models.ImageField(upload_to='img_projeto')
    titulo = models.CharField(max_length=70)
    descricao = models.TextField()

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo

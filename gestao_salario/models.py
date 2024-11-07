from django.db import models
from django.contrib.auth.models import User


class Salario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Associa ao usuário logado
    salario = models.FloatField(max_length=25)

    def __str__(self):
        return f"{self.usuario.username} - {self.salario}"

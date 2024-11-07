from django.db import models
from django.contrib.auth.models import User


class Salario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Associa ao usuário logado
    salario = models.FloatField()  # max_length não é necessário para FloatField

    def __str__(self):
        return str(self.salario)

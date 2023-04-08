from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField("Nome", max_length=100)
    idade = models.PositiveIntegerField("Idade")

    def __str__(self):
        return self.nome


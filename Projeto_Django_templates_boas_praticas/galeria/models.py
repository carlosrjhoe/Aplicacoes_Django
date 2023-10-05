from django.db import models

# Create your models here.

class Cavaleiro(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    constelacao = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)

    objects = models.Manager()

    def __str__(self) -> str:
        return f'{self.nome} - {self.constelacao}'
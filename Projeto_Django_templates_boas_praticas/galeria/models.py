from django.db import models

# Create your models here.
class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    foto = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='imagem')

    objetos = models.Manager()
        
    def __str__(self) -> str:
        return f'Nome: {self.nome} - Legenda: {self.legenda}'
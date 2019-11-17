from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField(null=True, blank=True)
    foto = models.ImageField(upload_to='clientes_fotos', null=True, blank=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

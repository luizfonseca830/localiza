from django.db import models


class Automovel(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    placa = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='automoveis_fotos', null=True, blank=True)

    def __str__(self):
        return self.marca + ' ' + self.modelo + ' ' + self.placa

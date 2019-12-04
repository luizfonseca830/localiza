from django.db import models
from clientes.models import Cliente
from automoveis.models import Automovel


class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    automovel = models.ForeignKey(Automovel, null=False, blank=False, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_inicio = models.DateField()
    data_final = models.DateField()
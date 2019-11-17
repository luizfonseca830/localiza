from django.forms import ModelForm
from clientes.models import Cliente


# Herança de modelForm
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'idade', 'foto']

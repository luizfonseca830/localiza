from django.forms import ModelForm
from automoveis.models import Automovel


# Herança de modelForm
class AutomovelForm(ModelForm):
    class Meta:
        model = Automovel
        fields = ['marca', 'modelo', 'placa', 'alugado', 'foto']

from django.forms import ModelForm
from locadora.models import Locacao


# Herança de modelForm
class LocacaoForm(ModelForm):
    class Meta:
        model = Locacao
        fields = ['cliente', 'automovel', 'valor']

from django.forms import ModelForm, DateField
from locadora.models import Locacao


# Herança de modelForm
class LocacaoForm(ModelForm):
    data_inicio = DateField(input_formats=['%d/%m/%Y'])
    data_final = DateField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Locacao
        fields = '__all__'

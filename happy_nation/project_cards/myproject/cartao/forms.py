from django import forms
from .models import Cartao

class CartaoForm(forms.ModelForm):
    class Meta:
        model = Cartao
        fields = ['nome_titular', 'numero_cartao', 'data_validade', 'codigo_seguranca']
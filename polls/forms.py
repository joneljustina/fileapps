from django import forms

from .models import livroEntrada, livroSaida

class livroEntradaForm(forms.ModelForm):
    class Meta:
        model = livroEntrada
        fields =("__all__") #('__all__')
# livroEntrada("numeroEntrada","dataEntrada","numeroDocumento","dataDocumento","providencia","assunto","classificacao","obsevacao","documento"

class livroSaidaForm(forms.ModelForm):
    class Meta:
        model = livroSaida
        fields = ('__all__')

# livroEntrada("numeroEntrada","dataEntrada","numeroDocumento","dataDocumento","providencia","assunto","classificacao","obsevacao","documento"

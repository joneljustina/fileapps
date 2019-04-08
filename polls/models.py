from django.db import models
from datetime import date

# Create your models here.

# Obsevacao todo documento dever ser dado entrada
class livroEntrada(models.Model):
    numeroEntrada = models.IntegerField("Número de entrada")
    dataEntrada = models.DateField("Introduza a data de entrada do documento")
    numeroDocumento = models.IntegerField("Número do documento",primary_key=True) 
    dataDocumento = models.DateField("Número do documento",null=True,default=date.today)
    proveniencia = models.CharField("Proveniência", null=True, max_length=100)
    assunto = models.CharField("Assunto",null=True, max_length=100)
    classificacao = models.CharField("Classificação", null=True, max_length=100) 
    observacao = models.CharField("Observação",null=True, max_length=100)
    documento = models.FileField("Documento",null=True, upload_to='correspondencia/documento')

    def __str__(self):
        return self.numeroDocumento
"""
#imagem = models.
# livroEntrada("numeroEntrada","dataEntrada","numeroDocumento","dataDocumento","providencia","assunto","classificacao","obsevacao","documento"

# Obsevacao : cada documento que sai foi dado entrada
# livroSaida("livroEntrada","numeroOrdem","classificacao","processo","data","destinatario","localidade","assunto","observacao"
"""
class livroSaida(models.Model):
    livroEntrada = models.ForeignKey('livroEntrada', on_delete=models.CASCADE)
    numeroOrdem = models.CharField("Número de ordem",max_length=100) #AutoField()AssertionError: Model polls.livroSaida can't have more than one AutoField.
    classificacao = models.CharField("Introduz a classificação",null=True, max_length=100)
    processo = models.CharField("Introduza o número do processo",null=True, max_length=50)
    data = models.DateField("Introduza da data de saída do documento",null=True, default=date.today )
    destinatario = models.CharField("Introduza o destinatário do documento", null=True, max_length=100)
    localidade = models.CharField("Introduza a localidade do documento", null=True, max_length=100)    
    assunto = models.CharField("Introduza o assunto do documento", null=True, max_length=100)
    observacao = models.CharField("Introduza a observacao do documento", null=True, max_length=100)

    def __str__(self):
        return self.numeroOrdem



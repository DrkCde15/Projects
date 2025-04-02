from django.db import models

class Cartao(models.Model):
    nome_titular = models.CharField(max_length=100)
    numero_cartao = models.CharField(max_length=16)
    data_validade = models.CharField(max_length=5)
    codigo_seguranca = models.CharField(max_length=3)
    senha_cartao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_titular} - ****{self.numero_cartao[-4:]}"
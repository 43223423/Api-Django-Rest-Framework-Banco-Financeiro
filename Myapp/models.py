from django.db import models

from uuid import uuid4

# Create your models here.

from django.contrib.auth.models import User

from django.shortcuts import render

def upload_image(instance, filename):
    return f'{instance.id}-{filename}'

from django.core.validators import MinValueValidator, MaxValueValidator

class Usuario(models.Model):
    nomeUsuario = models.CharField(max_length=80, null=False)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=100, null=False)
    imagem = models.ImageField(upload_to=upload_image, blank=False, null=False)

    def __str__(self):
        return str(self.nomeUsuario)


class Cliente(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=80, null=False)
    rg = models.FloatField(max_length=11, null=False)
    idade = models.FloatField(max_length=5, null=False)
    numero = models.FloatField(max_length=19, null=False)
    Usuario_Cliente = models.ForeignKey(Usuario, related_name='Usuario_Cliente', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nome)



class Transacoes(models.Model):
    id_transacao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10000, default=False)
    valor = models.DecimalField(max_digits=10000, decimal_places=2,
                                validators=[MinValueValidator(0.00, message='O valor deve ser no mínimo 0.00'),
                                            MaxValueValidator(1000000)])
    data_transacao = models.DateTimeField(auto_now=True)
    descricao = models.CharField(max_length=120, default='0')



class Endereco(models.Model):
    Cliente_endereco = models.ForeignKey(Cliente, related_name='Cliente_Endereco', on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=100, null=False)
    bairro = models.CharField(max_length=50, null=False)
    cidade = models.CharField(max_length=50, null=False)
    cep = models.CharField(max_length=10, null=False)


class Conta(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    agencia = models.CharField(max_length=10, null=False)
    numero = models.CharField(max_length=25, null=False)
    saldoBancario = models.FloatField(max_length=100000, null=False, default=0)
    Cliente_Conta = models.ForeignKey(Cliente,  related_name='Conta_Cliente', on_delete=models.CASCADE)

    def __str__(self) :
        return str(self.codigo)


class Emprestimo(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    emprestimo_Conta = models.ForeignKey(Conta, related_name='Emprestimo_Conta', on_delete=models.CASCADE)
    dataSolicitacao = models.DateTimeField(auto_now=True)
    valorSolicitado = models.CharField(max_length=1000000, null=False)
    numeroParcela = models.CharField(max_length=10, null=False)
    obervacao = models.CharField(max_length=200, null=True)


from Myapp import models
from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


from uuid import uuid4

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    id = serializers.models.AutoField(primary_key=True)
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'is_superuser', 'is_staff']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializers, self).create(validated_data)


class TransacoesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Transacoes
        fields = '__all__'


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Endereco
        fields = '__all__'


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Conta
        fields = '__all__'


class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emprestimo
        fields = '__all__'
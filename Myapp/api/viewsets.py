from Myapp import models
from Myapp.api import serializers
from rest_framework import viewsets

from rest_framework.generics import CreateAPIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()
    permission_classes = [IsAuthenticated,]

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsuarioSerializer
    queryset = models.Usuario.objects.all()
    #permission_classes = [IsAuthenticated,]

class CreateViewSet(CreateAPIView):
    model = User
    serializer_class = serializers.UserSerializers
    #permission_classes = [IsAuthenticated,]

# class CustomToken(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         Response = super().post(request, *args, **kwargs)
#         user_id = self.user.id
#         Response.data['user_id'] = user_id
#         return Response


class TransacoesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransacoesSerializers
    queryset = models.Transacoes.objects.all()
    permission_classes = [IsAuthenticated,]


class EnderecoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EnderecoSerializer
    queryset = models.Endereco.objects.all()

class ContaViewSet(viewsets.ModelViewSet):
    serializer_class =  serializers.ContaSerializer
    queryset = models.Conta.objects.all()
    #permission_classes = [IsAuthenticated,]


class EmprestimoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmprestimoSerializer
    queryset = models.Emprestimo.objects.all()
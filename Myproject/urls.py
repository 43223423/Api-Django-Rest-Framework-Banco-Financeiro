"""
URL configuration for Myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from Myapp.api import viewsets

from django.conf.urls.static import static
from django.conf import settings

from Myapp.views import customer_detail

route = routers.DefaultRouter()

route.register(r'Clientes', viewsets.ClienteViewSet, basename='Cliente')
route.register(r'Usuarios', viewsets.UsuarioViewSet, basename='Usuario')
route.register(r'Transacoes', viewsets.TransacoesViewSet, basename='Transacoes')
route.register(r'Endereco', viewsets.EnderecoViewSet, basename='Endereco')
route.register(r'ContaBancaria', viewsets.ContaViewSet, basename='ContaBancaria')
route.register(r'Emprestimo', viewsets.EmprestimoViewSet,basename='Emprestimo')


from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('Myapp.urls')),
    path('', include(route.urls)),
    path('create_user/', csrf_exempt(viewsets.CreateViewSet.as_view())),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh', TokenObtainPairView.as_view()),
    path('customers/<int:forekey>/',customer_detail, name='customer' )


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

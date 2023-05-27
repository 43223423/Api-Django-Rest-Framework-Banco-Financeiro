from django.shortcuts import render
from . import views
# Create your views here.

from django.http import HttpResponse

from django.contrib.auth.models import User

from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import Cliente

def home(request):
    return HttpResponse('Olaa')


def customer_detail(request, forekey):
    try:
        customer = Cliente.objects.get(id=forekey)
        data = {
            'name': Cliente.nome,
            'email': Cliente.idade,
            'phone': Cliente.numero
        }
        return JsonResponse(data)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Customer not found'}, status=404)



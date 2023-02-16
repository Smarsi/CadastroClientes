from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

#fazendo import dos models
from .models import Cliente

#fazendo import dos serializers 
from .serializers import ClienteSerializer

class CadCustumer(APIView):
    def post(self, request, format=None):
        reponse = []
        dados = request.data
        print(dados)

        serializer = ClienteSerializer(data=dados)

        if serializer.is_valid():
            serializer.save()
            return Response('Cliente cadastrado com sucesso', status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetAllCostumers(APIView):
    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)





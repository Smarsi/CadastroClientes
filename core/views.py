from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

#fazendo import dos models
from .models import Cliente

#fazendo import dos serializers 
from .serializers import ClienteSerializer

#import para fazer verificação de CPF
from .verificar_cpf import VerificaCPF

class CadCustumer(APIView):
    def post(self, request, format=None):
        reponse = []
        dados = request.data
        new_cpf = VerificaCPF(dados['cpf'])
        if new_cpf['is_valid'] == True:
            dados['cpf'] = new_cpf['cpf_tratado']
            serializer = ClienteSerializer(data=dados)
            if serializer.is_valid():
                serializer.save()
                return Response('Cliente cadastrado com sucesso', status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Erro - CPF Inválido \n Por favor digite um CPF válido', status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
class GetAllCostumers(APIView):
    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)





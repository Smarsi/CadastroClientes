from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

#fazendo import dos models
from .models import Cliente

#fazendo import dos serializers 
from .serializers import ClienteSerializer

#import para fazer verificação de CPF
from .verificar_cpf import CheckCPF

class CadCustumer(APIView):
    def post(self, request, format=None):
        reponse = []
        dados = request.data
        new_cpf = CheckCPF(dados['cpf'])
        print(new_cpf)
        if new_cpf['is_valid'] == True:
            dados['cpf'] = new_cpf['new_cpf']
            serializer = ClienteSerializer(data=dados)
            if serializer.is_valid():
                serializer.save()
                return Response('Cliente cadastrado com sucesso', status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Erro - CPF Inválido *** Por favor digite um CPF válido ***', status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                    
class GetAllCustumers(APIView):
    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetCustumer(APIView):
    def get(self, request, format=None):
        cliente = Cliente.objects.filter(pk=request.query_params['id'][0])
        if cliente:
            serializer = ClienteSerializer(cliente, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Nenhum usuário foi encontrado com o ID fornecido', status=status.HTTP_404_NOT_FOUND)


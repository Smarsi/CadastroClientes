from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

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
                    
class GetAllCustumers(APIView, LimitOffsetPagination):

    def get(self, request, format=None):
        clientes = self.paginate_queryset(queryset=Cliente.objects.all(), request=request)
        #clientes = self.paginate_queryset(Cliente.objects.all())
        serializer = ClienteSerializer(clientes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetCustumer(APIView):
    def get(self, request, format=None):
        if request.query_params.get('id', None):
            cliente = Cliente.objects.filter(pk=request.query_params.get('id', None))
        elif request.query_params.get('nome', None):
            cliente = Cliente.objects.filter(nome=request.query_params.get('nome', None))
        elif request.query_params.get('cpf', None):
            cpf_check=request.query_params.get('cpf', None)
            if len(cpf_check.split('.')) > 1 or len(cpf_check.split('-')) > 1 or len(cpf_check) > 11:
                return Response('Por favor verifique o CPF passado. Para realizar pesquisa usando cpf digite apenas os 11 números (sem pontos ou traços).', status=status.HTTP_400_BAD_REQUEST)
            else:
                cliente = Cliente.objects.filter(cpf=request.query_params.get('cpf', None))                
        else:
            return Response('Por favor forneça um valor para pesquisar um cliente (id, nome ou cpf)', status=status.HTTP_400_BAD_REQUEST)
        if cliente:
            serializer = ClienteSerializer(cliente, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Nenhum usuário foi encontrado com o ID fornecido', status=status.HTTP_400_BAD_REQUEST)
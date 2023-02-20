from rest_framework import serializers
from django.contrib.auth.models import User, Group

#importando os models
from .models import *

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'nascimento']
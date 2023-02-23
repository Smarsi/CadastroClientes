from django.test import TestCase
from model_mommy import mommy

from core.models import Cliente

'''
    Este arquivo executa os testes nos models do projeto.
    Iremos testar a criação de um cliente usando o modelmommy (biblioteca que cria elementos aleatorios dentro dos models do django).
'''


class ClienteTestCase(TestCase):
    
    def setUp(self):
        self.nome = "usuario de testes"
        self.cpf = "12345678911"
        self.nascimento = "1975-05-21"

    def test_create_cliente(self):
        cliente = Cliente(self.nome, self.cpf, self.nascimento)
        print(cliente)
        self.assertTrue(cliente, self.nome)

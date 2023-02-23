from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from django.http import QueryDict
import json

from core.views import GetAllCustumers, GetCustumer, CadCustumer
from core.models import Cliente

class GetAllCustumersTestCase(TestCase):

    def setUp(self):
        self.cliente_http = Client()

    def test_get_all_custumers(self):
        request = self.cliente_http.get(reverse_lazy('consult-all-custumers'))
        self.assertEqual(request.status_code, 200) #espera-se que a view retorne 200(sucesso)

class GetCustumerTestCase(TestCase):

    def setUp(self):
        self.cliente_http = Client()

        self.custumer = Cliente.objects.create(nome="TesteView", cpf="12345678911", nascimento="2021-08-01")

    def test_get_custumer_byName(self):
        request = self.cliente_http.get(reverse_lazy('consult-custumer')+"?nome="+self.custumer.nome)
        data = (dict(request.data[0]))

        self.assertEqual(self.custumer.nome, data['nome'])
    
    def test_get_custumer_byCpf(self):
        request = self.cliente_http.get(reverse_lazy('consult-custumer')+"?cpf="+self.custumer.cpf)
        data = (dict(request.data[0]))

        self.assertEqual(self.custumer.cpf, str(data['cpf']))

    def test_get_custumer_byId(self):
        request = self.cliente_http.get(reverse_lazy('consult-custumer')+"?id="+str(self.custumer.pk))
        data = (dict(request.data[0]))

        self.assertEqual(self.custumer.id, data['id'])    

class CadCustumerTestCase(TestCase):

    def setUp(self):
        self.cliente_http = Client()
        self.data_cpf_valid = {
            'nome': 'Usuario1',
            'cpf': '841.045.330-41',
            'nascimento': '1986-11-07'
        }
        self.data_cpf_valid = json.dumps(self.data_cpf_valid)
        self.data_cpf_invalid = {
            'id': '',
            'nome': 'Usuario1',
            'cpf': '125.126.476-34',
            'nascimento': '1986-11-07'
        }        
        
    def test_cad_custumer_valid(self):
        #print(self.data_cpf_valid)
        request = self.cliente_http.post(reverse_lazy('new-custumer'), data=self.data_cpf_valid, content_type='application/x-www-form-urlencoded', format='multipart')
        self.assertEqual(request.status_code, 200) #Deve cadastrar com sucesso
    
    ''' def test_cad_custumer_invalid(self):
        request = self.cliente_http.post(reverse_lazy('new-custumer'), data=QueryDict(self.data_cpf_invalid), content_type='application/x-www-form-urlencoded')
        self.assertEqual(request.status_code, 422) #Deve retornar 422 e mensagem de cpf inválido'''
from django.test import TestCase

from core.verificar_cpf import CheckCPF, _ExecuteCount


class CpfTestCase(TestCase):
    
    def setUp(self):
        self.cpf = '680.363.780-86'
        self.cpf_sem_caracteres = '68036378086'
        self.lista = ['6','8','0','3','6','3','7','8','0','8','6']
        self.cpf_invalido = '682.368.740-21'
        self.cpf_invalido_sem_caracteres = '68236874021'
        self.lista_invalido = ['6','8','2','3','6','8','7','4','0','2','1']
        self.lista_invalido_sem_digito = ['6','8','2','3','6','8','7','4','0']
        self.cpf_com_menos_de_11_digitos = '456.51.2148'

    def test_calc_cpf(self):
        cpf = CheckCPF(self.cpf)
        cpf_invalido = CheckCPF(self.cpf_invalido)
        cpf_menos_11_digitos = CheckCPF(self.cpf_com_menos_de_11_digitos)

        self.assertEqual(self.cpf_sem_caracteres, cpf['new_cpf']) # Deve retornar igual
        self.assertNotEqual(self.cpf_invalido_sem_caracteres, cpf_invalido['new_cpf']) # Deve retornar diferente
        self.assertEqual('', cpf_menos_11_digitos['new_cpf'])

    def test_executeCount(self):
        count = _ExecuteCount(self.lista)
        count_invalido = _ExecuteCount(self.lista_invalido_sem_digito) #a função espera uma lista sem os dois ultimos digitos do cpf

        self.assertEqual(self.lista, count)
        self.assertNotEqual(self.lista_invalido, count_invalido) # O retorno da função retornará um cpf válido que é diferente do cpf inválido passado (deve retornar "Not Equal")
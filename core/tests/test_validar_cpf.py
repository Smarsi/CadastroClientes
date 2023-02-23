from django.test import TestCase

from core.verificar_cpf import CheckCPF, _ExecuteCount


class CpfTestCase(TestCase):
    
    def setUp(self):
        self.cpf = '141.285.256-00'


    def test_calc_cpf(self):
        cpf = CheckCPF(self.cpf)

        self.assertTrue(cpf, self.cpf)
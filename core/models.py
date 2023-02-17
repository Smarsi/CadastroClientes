from django.db import models

# Create your models here.
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add = True)
    modificado = models.DateField('Modificado', auto_now = True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Cliente(Base):
    nome = models.CharField('Nome', max_length=200, blank=False, null=False)
    cpf = models.BigIntegerField('CPF', unique=True, blank=False, null=False)
    nascimento = models.DateField('Data de Nascimento', auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return str(self.nome + ' - CPF:'+ str(self.cpf))
    
class Endereco(Base):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    logradouro = models.CharField('Logradouro', max_length=200, null=False, blank=False)
    numero = models.CharField('Numero', max_length=50, null=False, blank=False)
    complemento = models.CharField('Complemento', max_length=50)
    bairro = models.CharField('Bairro', max_length=100, null=False, blank=False)
    cidade = models.CharField('Cidade', max_length=100, null=False, blank=False)
    estado = models.CharField('Estado', max_length=100, null=False, blank=False)
    cep = models.CharField('Cep', max_length=8, null=False, blank=False)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        if self.complemento:
            return str(self.logradouro + ', nº'+self.numero+', '+self.complemento+', '+self.bairro+', '+self.cidade+', '+self.estado)
        else:
            return str(self.logradouro + ', nº'+self.numero+', '+self.bairro+', '+self.cidade+', '+self.estado)
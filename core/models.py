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
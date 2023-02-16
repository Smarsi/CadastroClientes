#Contém função que será usada para verificar a validade de CPFs durante o cadastro de clientes.


def VerificaCPF(cpf):
    cpf_tratado = str(cpf).replace('.','').replace('-','')
    response = {'is_valid?': False, 'cpf_tratado': None}
    if int(cpf_tratado):
        #calculo para verificar se o CPF é valido
        response['is_valid'] = True
        response['cpf_tratado'] = cpf_tratado
        return response
    else:
        return response
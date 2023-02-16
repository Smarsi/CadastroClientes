#Contém função que será usada para verificar a validade de CPFs durante o cadastro de clientes.


def _ExecuteCount(lista):
    while len(lista) < 11:
        num = len(lista)+1
        nova_lista = []
        for i in lista:
            nova_lista.append(int(i) * num)
            num = num-1
        rest = sum(nova_lista) % 11
        if rest < 2:
            lista.append(str(0))
        elif rest >= 2:
            lista.append(str(11-rest))
    return lista

def CheckCPF(cpf):
    response = {'is_valid': False, 'new_cpf': ''}
    cpf = cpf.replace('-',"").replace('.',"")
    if len(cpf) == 11: #se o cpf tiver 11 digitos.
        cpf = list(cpf)
        new_cpf = list(cpf)
        del new_cpf[9:11]
        new_cpf = _ExecuteCount(new_cpf)        
        if new_cpf == cpf: 
            response['new_cpf'] = ''.join(new_cpf)
            response['is_valid'] = True
            return response
        else:
            return response
    else: #se o cpf tiver menos de 11 digitos.
        return response
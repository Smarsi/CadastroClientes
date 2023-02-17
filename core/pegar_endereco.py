import requests

def GetAddresByCEP(cep):
    cep = cep.replace('.', '').replace('-','')
    if len(cep) == 8:
        link = f'https://viacep.com.br/ws/{cep}/json/'
        response =  requests.get(link)
        if response.status_code == 200:
            response = response.json()
            logradouro =  response['logradouro']
            bairro = response['bairro']
            cidade = response['localidade']
            estado = response['uf']

            result = {
            'logradouro': logradouro,
            'bairro': bairro,
            'cidade': cidade,
            'estado': estado,
            'cep': cep
            }
            return result
        
        elif response.status_code == 400:
            return 'Bad Request. Verifique se o CEP informado está correto.'
    else:
        return 'Bad Request. O número do CEP está incorreto.'
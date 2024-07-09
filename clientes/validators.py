import re
from validate_docbr import CPF

def validate_cpf(cpf):
    cpf = CPF()
    return validate_cpf(cpf)

def validate_name(nome):
    return nome.isalpha()

def validate_rg(rg):
    return len(rg) == 9

def validate_number(celular):
    '''
    Verifica se o celuar é válido. Ex.:11 94990-2159
    '''
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)

    return resposta

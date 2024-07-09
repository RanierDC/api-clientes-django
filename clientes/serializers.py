from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'O número do CPF inválido'})
    
        if not validate_name(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua números neste campo'})
        
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve ter 9 dígitos'})
        
        if not validate_number(data['celular']):
            raise serializers.ValidationError({'ceular':'A estrutura do celular não é válida'})
        return data
    
    '''
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve ter 11 dígitos")
        return cpf
    
    def validate_name(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("Não inclua números neste campo")
        return nome
    
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("O RG deve ter 9 dígitos")
        return rg
    
    def validate_number(self, celular):
        if len(celular) != 11:
            raise serializers.ValidationError("O Celular deve ter 11 dígitos")
        return celular
    '''
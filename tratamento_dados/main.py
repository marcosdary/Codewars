import json
import os
from dataclasses import dataclass
from functools import reduce
from datetime import date

FILE = os.path.dirname(__file__)+'\\pessoas.json'

class Open:
    def __init__(self, operacao:str) -> None:
        self.caminho = FILE
        self.operacao = operacao
        self.arquivo = None

    def __enter__(self):
        file = open(self.caminho, self.operacao, encoding='utf-8')
        self.arquivo = file

        return file
    
    def __exit__(self, cls, excep, trace) -> bool | Exception:
        self.arquivo.close()
        if excep is not None:
            raise cls(excep)
        return True

with Open('r') as file:    
    datas = json.load(file)

PERSON_AMOUNT = len(datas)
AVERAGE_AGE = reduce(
    lambda ac, data: ac + (2024 - date.fromisoformat(data['data_nascimento']).year),
    datas, 0
)

def isCpf(cpf:str):
    cpf = cpf.replace(".", '').replace('-', '')
    if cpf == 11:
        return False
    
    digito_verificador = 0
    for i in range(len(cpf[:9])):
        d = 10 - i
        if d > 1:
            digito_verificador += int(cpf[i]) * d
            
    digito_verificador = (digito_verificador * 10) % 11
    if digito_verificador == 10 or digito_verificador == 11:
        digito_verificador = 0
    
    if digito_verificador != int(cpf[9]):
        return False
    
    digito_verificador = 0
    for i in range(len(cpf[:10])):
        d = 11 - i
        if d > 1:
            digito_verificador += int(cpf[i]) * d
            
    digito_verificador = (digito_verificador * 10) % 11
    if digito_verificador == 10 or digito_verificador == 11:
        digito_verificador = 0
    if digito_verificador != int(cpf[10]):
        return False
    
    return True

@dataclass
class Person:
    name: str
    age: int 
    phone: str
    cpf: str

    def __str__(self) -> str:
        return f'Nome: {self.name}\nTelefone: {self.phone}\nIdade: {self.age}'
    
    @property
    def max_age(self) -> str:
        if self.age >= AVERAGE_AGE / PERSON_AMOUNT:
            return 'Sua idade é maior que a média do dados levantados' 
        return 'Sua idade é menor que a média do dados levantados'    

    def is_cpf(self) -> bool:
        return isCpf(self.cpf)     

for data in datas:
    age = 2024 - date.fromisoformat(data['data_nascimento']).year
    person = Person(data['nome'], age, data['numero_celular'], data['cpf'])
    print(person)
    print(person.max_age)
    print(f'CPF: {person.is_cpf()}')
    print()


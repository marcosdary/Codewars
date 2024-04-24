def decorator(func):
    def inner_function(*args, **kwargs):
        for arg in args:
            if isinstance(arg, int):
                validacao_idade(arg)
            elif isinstance(arg, str):
                validacao_nome(arg)
        return func(*args, **kwargs)
    return inner_function


def validacao_nome(nome:str):
    if all(x.isspace() or x.isalpha() for x in nome):
        return nome
    raise ValueError("Nome inválido")


def validacao_idade(idade:int):
    if idade > 0:
        return idade
    raise ValueError("Idade inválida")    


class Pessoa:

    def __init__(self) -> None:
        self._nome = None
        self._idade = None
        self.__endereco = None
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    @decorator
    def nome(self, nome:str):
        self.__nome = nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    @decorator
    def idade(self, idade:int):
        self._idade = idade 
        
    @property
    def endereco(self):
        return self.__endereco
   
    def endereco_pessoa(self, rua:str, numero:int):
        if validacao_nome(rua) and numero > 0:
            self.__endereco = {"rua": rua, "numero": numero}
            print("Seu endereço está correto")
        else:
            print("Seu endereço está incorreto")
            
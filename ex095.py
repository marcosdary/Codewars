from enum import Enum
# Crie um enum chamado NivelAcesso com os níveis de acesso de um sistema 
# (administrador, moderador e usuário) e adicione as permissões de cada nível. 
# Utilize o enum para controlar o acesso às funcionalidades do sistema.

class NivelAcesso(Enum):
    ADM = ('Administrador', 1, '@ba489')
    MOD = ('Moderador', 2, '%vayda78')
    USER = ('Usuário', 3, None)

    def __init__(self, categoria, nivel, senha) -> None:
        self.categoria = categoria
        self.nivel = nivel
        self.senha = senha

    @classmethod
    def acesso(cls, categoria, senha=None):
        try:
            CATEGORIA = cls[categoria]
            if CATEGORIA.value[2] == senha:
                return 'Acesso permitido'
            return 'Acesso negado'
        except KeyError:
            return 'Categoria não encontrada'
        
# Crie um enum chamado Moeda com as principais moedas do mundo (real, dólar, euro) 
# e adicione um atributo taxa_cambio para cada moeda. Utilize o enum para converter 
# valores entre diferentes moedas.

class Moeda(Enum):

    REAL = 'BRL', 1
    DOLAR = 'US', 5.4839
    EURO = 'EUR', 5.9385

    def __init__(self, nome, cambio) -> None:
        self.nome = nome
        self.cambio = cambio


def taxa_cambio(moeda:Moeda, paramoeda:Moeda, valor:float):
    if valor < 1:
        raise ValueError('Valor da moeda não permitido')
    
    if isinstance((moeda, paramoeda), Moeda):
        raise KeyError('Moeda não encontrada')

    valor = valor * Moeda[moeda].cambio
    novo_valor = round(valor / Moeda[paramoeda].cambio, 2)
    return f'{Moeda[moeda].nome} => {Moeda[paramoeda].nome}: {novo_valor} {Moeda[paramoeda].nome}'


# Crie um enum base chamado Veiculo com os tipos de veículos (carro, moto, caminhão) e 
# adicione um atributo marca para cada tipo. Crie enums derivados de Veiculo 
# para cada tipo de veículo, adicionando atributos específicos de cada tipo 
# (modelo, ano, capacidade de carga). Utilize os enums para gerenciar informações 
# sobre diferentes tipos de veículos.

class Veiculo(Enum):

    CARRO = 'Fiat'
    MOTO = 'Honda'
    CAMINHAO = 'Mercedes'

    def __init__(self, nome) -> None:
        self.nome = nome

class Carro:
    
    def __init__(self, modelo, ano, compartimento) -> None:
        self.veiculo = Veiculo.CARRO
        self.modelo = modelo
        self.ano = ano
        self.compartimento = compartimento

class Moto:

    def __init__(self, modelo, ano) -> None:
        self.veiculo = Veiculo.MOTO
        self.modelo = modelo
        self.ano = ano
    
class Caminhao:

    def __init__(self, modelo, ano, capacidade) -> None:
        self.veiculo = Veiculo.CAMINHAO
        self.modelo = modelo
        self.ano = ano
        self.capacidade = capacidade

# Crie um enum chamado EstadoCivil com os estados civis possíveis 
# (solteiro, casado, divorciado, viúvo) e defina valores personalizados 
# para cada estado civil (0, 1, 2, 3). Utilize o enum para armazenar 
# informações sobre o estado civil de uma pessoa.

class EstadoCivil(Enum):
    SOLTEIRO = ('solteiro', 0)
    CASADO = ('casado', 1)
    DIVORCIADO = ('divorciado', 2)
    VIUVO = ('viúvo', 3)

    def __init__(self, nome, indice) -> None:
        self.nome = nome
        self.indice = indice

class Pessoa:
    def __init__(self, nome_completo, nascimento, estado_civil, cpf) -> None:
        self.nome_completo = nome_completo
        self.nascimento = nascimento
        self.estado_civil = {'status': EstadoCivil[estado_civil].nome, 'indice': EstadoCivil[estado_civil].indice} if tuple(s.name for s in EstadoCivil) else None
        self.cpf = cpf

    def __str__(self):
        return f'{self.nome_completo}, seu estado civil é {self.estado_civil['status']}'
    

pessoa = Pessoa('Marcos Wyliam Silva Oliveira', '18/04/2004', 'SOLTEIRO', '999.999.999-48')
print(pessoa)

        



class Animal:
    def __init__(self, nome:str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        
    def fazer_som(self):
        return 'Som genérico de animal'

    @property
    def apresentar(self):
        return f'Olá, sou {self.nome} e sou um animal' 
  
    
class AnimalDomestico:
    def __init__(self, nome: str, idade: int, raca:str) -> None:
        self.nome = nome
        self.idade = idade      
        self.raca = raca
    
    def fazer_som(self):
        return 'Au au!!'
    
    @property
    def mostrar_raca(self):
        return f'Nome do raça: {self.raca}'
    

class Gato(AnimalDomestico, Animal):
    def __init__(self, nome: str, idade: int, raca:str) -> None:
        super().__init__(nome, idade, raca)
    
    def fazer_som(self):
        return 'Miau miau!!'
    
    @property
    def mostrar_raca(self):
        return super().mostrar_raca
    
class Cachorro(AnimalDomestico, Animal):
    def __init__(self, nome: str, idade: int, raca:str) -> None:
        super().__init__(nome, idade, raca)
    
    def fazer_som(self):
        return 'Au au!!'
    
    @property
    def mostrar_raca(self):
        return super().mostrar_raca
    

cachorro = Cachorro('Max', 11, 'Pastor alemão')
print(cachorro.apresentar) # Olá, sou Max e sou um animal
print(cachorro.mostrar_raca) # Nome do raça: Pastor alemão
print(cachorro.fazer_som()) # Au au!!
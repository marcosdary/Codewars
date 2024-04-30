class Veiculo:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano:int) -> None:
        super().__init__(marca, modelo)
        self.ano = ano
        
    def __str__(self):
        return f'Veículo: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}'
   
class Animal:
    def __init__(self, especie, nome) -> None:
        self.especie = especie
        self.nome = nome
        
class Cachorro(Animal):
    def __init__(self, especie, nome, raca:str) -> None:
        super().__init__(especie, nome)
        self.raca = raca
    def __str__(self):
        return f'Espécie: {self.especie}\nNome: {self.nome}\nRaça: {self.raca}'     
        
car = Carro('Fiat', 'Touro', 2023)
print(car)
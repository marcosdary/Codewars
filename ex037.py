class Veiculo:
    def __init__(self, modelo, cor, ano_de_fabricacao) -> None:
        self.moodelo = modelo
        self.cor = cor
        self.ano_de_fabricacao = ano_de_fabricacao
        
class Carro(Veiculo):
    def __init__(self, modelo, cor, ano_de_fabricacao):
        super().__init__(modelo, cor, ano_de_fabricacao)
        
    def __str__(self) -> str:
        return f'Veículo é um carro com as seguintes características:\n\tModelo: {self.moodelo}\n\tCor: {self.cor}\n\tAno de fabricação: {self.ano_de_fabricacao}'
    
class Moto(Veiculo):
    def __init__(self, modelo, cor, ano_de_fabricacao):
        super().__init__(modelo, cor, ano_de_fabricacao)
        
    def __str__(self) -> str:
        return f'Veículo é uma moto com as seguintes características:\n\tModelo: {self.moodelo}\n\tCor: {self.cor}\n\tAno de fabricação: {self.ano_de_fabricacao}'
    
class Bicicleta(Veiculo):
    def __init__(self, modelo, cor, ano_de_fabricacao):
        super().__init__(modelo, cor, ano_de_fabricacao)
        
    def __str__(self) -> str:
        return f'Veículo é uma bicicleta com as seguintes características:\n\tModelo: {self.moodelo}\n\tCor: {self.cor}\n\tAno de fabricação: {self.ano_de_fabricacao}'
    
car = Carro("Fiat", 'Rosa', 1994)
moto = Moto('Honda', 'Vermelha', 2021)
bic = Bicicleta("Yia", 'Preta', 2020)

print(bic)
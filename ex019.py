class PassagemArea:
    def __init__(self, origem, destino, data, assentos_disponiveis) -> None:
        self.origem = origem
        self.destino = destino
        self.data = data
        self.assentos_disponiveis = assentos_disponiveis
        
    def reserva_assento(self, quantidade):
        if quantidade <= self.assentos_disponiveis:
            self.assentos_disponiveis -= quantidade
            return f'Assento reservado com sucesso\nA quantidade de assentos igual a {quantidade}'
        else:
            return f'Infelizmente, a quantidade está acima dos assentos disponíveis'
    
    def __str__(self):
        return f'Detalhes\n\tOrigem: {self.origem}\n\tDestino: {self.destino}\n\tData: {self.data}\n\tAssentos Disponíveis: {self.assentos_disponiveis}'
        
latam = PassagemArea('São Paulo', 'Estados Unidos', "12/10/2025", 100)
print(latam)
print()
print(latam.reserva_assento(8))
print()
print(latam.reserva_assento(9))
print()
print(latam.reserva_assento(100))
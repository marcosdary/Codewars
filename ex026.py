# Classes:

# Crie uma classe Hotel com atributos como nome, endereço, lista de quartos, lista de reservas e capacidade total de hóspedes.
# Crie uma classe Quarto com atributos como número do quarto, tipo (simples, duplo, suíte), preço por noite e disponibilidade.
# Crie uma classe Hospede com atributos como nome, CPF, lista de reservas e histórico de estadias.

# Funcionalidades:

# Implemente métodos na classe Hotel para adicionar quartos, fazer reservas e verificar a disponibilidade de quartos para determinadas datas.
# Adicione métodos na classe Quarto para atualizar a disponibilidade e gerar relatórios de ocupação.
# Desenvolva métodos na classe Hospede para fazer reservas, cancelar reservas e calcular o total gasto em estadias.

class Hotel:
    def __init__(self, nome:str, endereco:str) -> None:
        self.nome = nome
        self.endereco = endereco
        self._capacidade_total = None
        self.__lista_quartos = []
        self.__lista_reservas = []
    
    @property
    def capacidade_total(self):
        return self._capacidade_total
    
    @capacidade_total.setter
    def capacidade_total(self, valor:int):
        
        if valor > 0:
            self._capacidade_total = valor
            
        else:
            print(f'Capacidade total: {False}')
    
    @property
    def lista_quartos(self):
        return self.__lista_quartos
    
    @lista_quartos.setter
    def lista_quartos(self, quarto):
        self.__lista_quartos.append(quarto)
    
    @property
    def lista_reservas(self):
        return self.__lista_reservas
            
    def fazer_reserva(self, quarto:str, data:str):
        
        if quarto in self.__lista_quartos:
            reserva = {'quarto': quarto, 'data': data}
            self.__lista_reservas.append(reserva)
        
        else:
            print(f'Reserva: {False}')
    
class Quarto:
    def __init__(self, num_quarto:int, tipo_quarto:str, data:str) -> None:
        self.num_quarto = num_quarto
        self.tipo_quarto = tipo_quarto
        self.data = data
        self.__preco = None
        self.__disponibilidade = True
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor:float):
        
        if valor > 0:
            self.__preco = valor
            
        else:
            print(f'Preço do quarto: {False}')
    
    @property
    def disponibilidade(self):
        return self.__disponibilidade
    
    def atualizar_disponibilidade(self, status):
        if status is False:
            self.__disponibilidade = False
        else:
            self.__disponibilidade = True
                   
    def __str__(self) -> str:
        print(f'Quarto: {self.num_quarto}\nTipo do quarto: {self.tipo_quarto}\nData: {self.data}\nPreço por noite: {self.__preco}\nDisponibilidade: {self.__disponibilidade}\n')
        return '' 
       
        
          
class Hospede:
    def __init__(self, nome:str, cpf:int) -> None:
        self.nome = nome
        self.cpf = cpf 
        self.__lista_reservas = []

    @property
    def lista_reservas(self):
        return self.__lista_reservas
    
    def historico_reservas(self):
        pass
    
    def inserir_reserva(self, quarto, hotel, data_reserva):
        filtro_hotel = list(filter(lambda h: h.disponibilidade is True, hotel.lista_quartos))
        if quarto in filtro_hotel:
            quarto.atualizar_disponibilidade(False)
            hotel.fazer_reserva(quarto, data_reserva)
            pedido_dict = {'quarto': quarto, 'hotel': hotel}
            self.__lista_reservas.append(pedido_dict)
    
        else:
            print(f'Hotel: {hotel.nome} não têm este quarto')
        
    def cancelar_reserva(self, quarto):
        quarto.atualizar_disponibilidade(True)
        for reserva in self.__lista_reservas:
            
            if reserva['quarto'] == quarto:
                index = self.__lista_reservas.index(reserva)
                self.__lista_reservas.pop(index)
                
        return '\tReserva cancelada com sucesso'
    
    def gasto_total(self):
        v = 0
        for reserva in self.__lista_reservas:
            print(f"Quarto: {reserva['quarto'].nome}\nPreço: {reserva['quarto'].preco}\n") 
            v += reserva['quarto'].preco
        print(f"Total gasto: {v}\n")
    
    def __str__(self) -> str:
        print(f'\tCliente: {self.nome}\n\tCPF: {self.cpf}\n')
        
        for reserva in self.__lista_reservas:
            print(f"Quarto: {reserva['quarto'].num_quarto}\nTipo de quarto: {reserva['quarto'].tipo_quarto}\nPreço: {reserva['quarto'].preco}\nHotel: {reserva['hotel'].nome}\n")   
        
        return ''
    

# Quarto
quart = Quarto(4512, 'Suíte', '10/01/2024')
quart.preco = 127

quart2 = Quarto(4612, 'Simples', '10/02/2024')
quart2.preco = 367.78

quart = Quarto(4513, 'Suíte', '10/01/2024')
quart.preco = 127

quart2 = Quarto(7512, 'Simples', '10/02/2024')
quart2.preco = 367.78

quart3 = Quarto(4582, 'Suíte', '10/01/2024')
quart3.preco = 127.45

quart4 = Quarto(1512, 'Duplo', '10/03/2024')
quart4.preco = 345.78

# Hotel

hot = Hotel('Novo Amanhã', 'São Bernardo')
hot.lista_quartos = quart
hot.lista_quartos = quart2
hot.capacidade_total = 1200

hot2 = Hotel('Novo Nascer', 'São Bernardo')
hot2.lista_quartos = quart
hot2.lista_quartos = quart3
hot2.capacidade_total = 5120

hot3 = Hotel('Palácio Novo', 'São Paulo')
hot3.lista_quartos = quart4
hot3.capacidade_total = 178

# Hospede

hosp = Hospede('Márcio', '123.478.784-94')
hosp.inserir_reserva(quart4, hot3, '10/03/2024')
hosp.inserir_reserva(quart2, hot, '10/02/2024')
#hosp.cancelar_reserva(quart2)
#hosp.cancelar_reserva(quart4)

hosp2 = Hospede('Mário', '123.446.784-21')
hosp2.inserir_reserva(quart, hot, '12/04/2024')
hosp2.inserir_reserva(quart3, hot2, '13/02/2024')
#hosp.cancelar_reserva(quart2)
#hosp.cancelar_reserva(quart4)
print(hot2.lista_reservas[0]['quarto'])
print(hosp2)
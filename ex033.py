# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor_nome:str):
        
        self._motor = motor_nome
            

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante_nome:str):
        self._fabricante = fabricante_nome
        


class Motor:
    def __init__(self, nome):
        self.nome = nome
            
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        
             
 

# Teste

motor_4_0 = Motor('4.0')
motor_1_0 = Motor('1.0')

volkswagen = Fabricante('Volkswagen')
fiat = Fabricante('Fiat')
toyota = Fabricante('Toyota')

saveiro = Carro('Saveiro')
saveiro.motor = motor_4_0
saveiro.fabricante = volkswagen


toro = Carro('Toro')
toro.motor = motor_4_0
toro.fabricante = fiat

uno = Carro('Uno')
uno.motor = motor_1_0
uno.fabricante = fiat

corolla = Carro('Corolla')
corolla.motor = motor_1_0
corolla.fabricante = toyota
 
print(saveiro.nome, saveiro.motor.nome, saveiro.fabricante.nome)
print(toro.nome, toro.motor.nome, toro.fabricante.nome)
print(uno.nome, uno.motor.nome, uno.fabricante.nome)
print(corolla.nome, corolla.motor.nome, corolla.fabricante.nome)



class Motor:
    def __init__(self) -> None:
        self._tipo = None
        self._potencia = None
        
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, valor:str):
        if valor.isalnum():
            self._tipo = valor
        else:
            raise ValueError("Tipo de motor incompável")
    
    @property
    def potencia(self):
        return self._potencia
    
    @potencia.setter
    def potencia(self, valor:int):
        if valor > 0:
            self._potencia = valor
        else:
            raise ValueError("Potência de motor incompável")
    
    def __str__(self) -> str:
        return f"Potência: {self._potencia} HP, Tipo do motor: {self._tipo}"
        
class Carro:
    def __init__(self) -> None:
        self._marca = None
        self._motor = None
        
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, valor:str):
        if valor.isalpha():
            self._marca = valor
        else:
            raise ValueError("Tipo de marca incompável")
    
    @property
    def motor(self):
        return self._motor
    
    def motor_carro(self, tipo:str, potencia:int):
        try:
            motor_carro = Motor()
            motor_carro.tipo = tipo
            motor_carro.potencia = potencia
            self._motor = motor_carro
        except ValueError:
            print("\n\tEscreva os dados corretamente\n\tPor favor...")
            
    def __str__(self):
        return f'Marca: {self._marca}, Motor -> {self._motor}'
class Carro:
    def __init__(self, quilometragem:float) -> None:
        self.quilometragem = quilometragem
        self._tanque = 0

    @property
    def gasolina(self):
        return self._tanque
    
    def andar(self, distancia:float):
        if distancia > 0:
            d = distancia/self.quilometragem
            if d < self._tanque:
                self._tanque -= d
            else:
                return 'Gasolina acabou, coloque gasolina'
            return True
        raise ValueError("Não há distância negativa")
    
    def adicionar_gasolina(self, litro):
        if litro > 0:
            self._tanque += litro
            return True
        raise ValueError("Não há volume negativo")
    
fusca = Carro(10)

fusca.adicionar_gasolina(20)
print(fusca.gasolina)
print(fusca.andar(100   ))
print(fusca.gasolina)


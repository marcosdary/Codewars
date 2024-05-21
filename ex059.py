from abc import ABC, abstractmethod
from math import sqrt

class Triangulo:
    
    def __init__(self, ld1, ld2, ld3) -> None:
        self.ld1, self.ld2, self.ld3 = self.__condicao_existencia(ld1, ld2, ld3)
        
    def __condicao_existencia(self, ld1, ld2, ld3):
        
        if ld1 + ld2 >= ld3 and ld2 + ld3 >= ld1 and ld1 + ld3 >= ld2:
            return ld1, ld2, ld3
        
        raise ValueError("Não atendeu a condição de existência")
    
    @abstractmethod
    def calculo_area(self): ...
    
class Equilatero(Triangulo):
    
    def __init__(self, ld1, ld2, ld3) -> None:
        self.__is_equilatero(ld1, ld2, ld3)
    
    def __is_equilatero(self, ld1, ld2, ld3):
        if ld1 == ld2 == ld3:
            return super().__init__(ld1, ld2, ld3)
        else:
            raise TypeError('Este Triângulo não é equilátero')
        
    def calculo_area(self):
        area = (pow(self.ld1, 2) * sqrt(3)) / 4
        return area
    
class Escaleno(Triangulo):
    
    def __init__(self, ld1, ld2, ld3) -> None:
        self.__is_escaleno(ld1, ld2, ld3)
    
    def __is_escaleno(self, ld1, ld2, ld3):
        if ld1 == ld2 or ld2 == ld3 or ld3 == ld1:
            return super().__init__(ld1, ld2, ld3)
        else:
            raise TypeError('Este Triângulo não é isósceles')
        
    def calculo_area(self):
        p = (self.ld1 + self.l2 + self.l3) / 2
        area = sqrt(p*(p-self.ld1)*(p-self.ld2)*(p-self.ld3))
        return area
        
class Isosceles(Triangulo):
    def __init__(self, ld1, ld2, ld3) -> None:
        self.__is_isosceles(ld1, ld2, ld3)
    
    def __is_isosceles(self, ld1, ld2, ld3):
        if ld1 == ld2 or ld2 == ld3 or ld3 == ld1:
            return super().__init__(ld1, ld2, ld3)
        else:
            raise TypeError('Este Triângulo não é isósceles')
        
    def calculo_area(self):
        h = sqrt(((self.ld1**2) - ((self.ld3 / 2)**2))) 
        area = (h * self.ld3) / 2
        return area
    



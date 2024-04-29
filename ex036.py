# Crie uma hierarquia de classes para representar figuras geométricas. 
# A classe base deve ser FiguraGeometrica, 
# com métodos para calcular área e perímetro. 
# Em seguida, crie classes específicas para círculo, 
# quadrado e triângulo, que herdam da classe FiguraGeometrica.
import math

class FiguraGeometrica:
    def area(self, a, fig_geo: str):
        return f'Área do/a {fig_geo}: {a}'
    
    def perimetro(self, a, fig_geo:str):
        return f'Perímetro do/a {fig_geo}: {a}'
    
class Quadrado(FiguraGeometrica):
    def __init__(self, lado:float):
        super().__init__()
        self.lado = lado
        
    def area(self):
        a = pow(self.lado, 2)
        return super().area(a, 'Quadrado')
    
    def perimetro(self):
        a = 4 * self.lado
        return super().perimetro(a, 'Quadrado')

class Triangulo(FiguraGeometrica):
    def __init__(self, base:float, altura:float, lda, ldb, ldc):
        super().__init__()
        self.base = base
        self.altura = altura
        self.lados = (lda, ldb, ldc)
        
    def area(self):
        a = (self.base * self.altura) / 2
        return super().area(a, 'Triângulo')
    
    def perimetro(self):
        a = sum(self.lados)
        return super().perimetro(a, 'Triângulo')

class Circulo(FiguraGeometrica):
    PI = math.pi
    def __init__(self, raio:float):
        super().__init__()
        self.raio = raio
        
    def area(self):
        a = self.PI * pow(self.raio, 2) 
        return super().area(round(a, 3), 'Círculo')
    
    def perimetro(self):
        a = 2 * self.PI * self.raio
        return super().perimetro(round(a, 3), 'Círculo')

qd1 = Quadrado(4)
print(qd1.area(), '\n', qd1.perimetro(), '\n')

tri1 = Triangulo(12, 8, 3, 4, 5)
print(tri1.area(),'\n', tri1.perimetro(), '\n')

cir1 = Circulo(3.75)
print(cir1.area(), '\n', cir1.perimetro())
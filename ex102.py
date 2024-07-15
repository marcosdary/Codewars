def Decorator(method_):
    def inner_funcition(self, *args, **kwds):
        m = method_(self, *args, **kwds)
        s = 0
        for n in m:
            s += sum(n)

        return True if s//9 >= 0 else False 
        
    return inner_funcition

class Matriz:
    def __init__(self, matriz:list[float]) -> None:
        self.matriz = matriz

    @Decorator
    def mutiplicacao(self, other) -> list[float]: 
        return [[x*y for x, y in zip(a, b)] for a, b in zip(self.matriz, other.matriz)]
    
matriz_1 = Matriz([
    [4, 4, 6],
    [21, 99, 48],
    [9, 12, 3]
])

matriz_2 = Matriz([
    [3, 3, 7],
    [20, 100, 38],
    [8, 13, 1]
])

print(matriz_1.mutiplicacao(matriz_2))  


# Crie uma classe base Animal com um método comer. 
# Em seguida, crie duas classes, Cachorro e Gato, 
# que herdam de Animal e sobrescrevem o método comer para imprimir uma mensagem específica.

class Animal:
    
    def __init__(self, nome):
        self.nome = nome
    
    def comer(self):
        print(f"O animal {self.nome} está comendo")
        return True
        
class Cachorro(Animal):
    
    def comer(self):
        print(f"O cachorro {self.nome} está comendo")
        return True

class Gato(Animal):
    
    def comer(self):
        print(f"O gato {self.nome} está comendo")
        return False


def mostrar_informacoes_animal(animal: Animal):
    
    animal_comeu = animal.comer()
    if animal_comeu:
        print("Está satisfeito")
    else:
        print("NÃO Está satisfeito")
        
mostrar_informacoes_animal(Cachorro("Max"))
mostrar_informacoes_animal(Gato("Manu"))

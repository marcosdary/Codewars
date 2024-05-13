from abc import ABC
class Pessoa(ABC):
    def __init__(self, nome, sobrenome, idade) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
    def mostrar_detalhes(self):
        
        print(f'Nome: {self.nome}\nSobrenome: {self.sobrenome}\nIdade: {self.idade}\nClasse: {self.__class__.__name__}\n\n')
        

class Professor(Pessoa):
    
    def __init__(self, nome, sobrenome, idade, lecionar, salario) -> None:
        super().__init__(nome, sobrenome, idade)
        self.__lecionar = lecionar
        self.salario = salario
    
    @property
    def lecionar(self):
        return self.__lecionar
        
class Medico(Pessoa):
    
    def __init__(self, nome, sobrenome, idade, area, salario) -> None:
        super().__init__(nome, sobrenome, idade)
        self.__area = area
        self.salario = salario
        
    @property
    def area(self):
        return self.__area


class Aluno(Pessoa):
    
    def __init__(self, nome, sobrenome, idade, pai, mae) -> None:
        super().__init__(nome, sobrenome, idade)
        self.__disciplinas = []
        self.pais = {'pai': pai, 'mae': mae}
        
    @property
    def disciplinas(self):
        return self.__disciplinas
    
    def adicionar_disciplina(self, *args):
        self.__disciplinas.append(*args)
        
medico = Medico('Marcos', 'Fernandes', 36, 'neurologia', 21_000)

professora = Professor('Cecília', 'Silver', 34, 'História', 13_200)

aluno = Aluno('Xavier', 'Matea', 14, medico, professora)
aluno.adicionar_disciplina(['História', 'Português', 'Artes', "Matemática"])

aluno.mostrar_detalhes()
professora.mostrar_detalhes()
medico.mostrar_detalhes()
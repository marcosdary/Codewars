from abc import ABC, abstractmethod

class Funcionario(ABC):
    
    def __init__(self, nome, nascimento, cpf, salario) -> None:
        self._nome = nome
        self._nascimento = nascimento
        self._cpf = cpf
        self._salario = salario
        
    @abstractmethod
    def get_bonificacao(self): ...
   
    @property 
    def salario(self):
        return self._salario
    
class Gerente(Funcionario):
    
    def __init__(self, nome, nascimento, cpf, salario, qtd_gerenciados) -> None:
        super().__init__(nome, nascimento, cpf, salario)
        self.qtd_gerenciados = qtd_gerenciados 
        
    def get_bonificacao(self):
        self._salario += round(self._salario * 0.14, 2)
    
class Designer(Funcionario):
    
    def __init__(self, nome, nascimento, cpf, salario) -> None:
        super().__init__(nome, nascimento, cpf, salario)
        
    def get_bonificacao(self):
        self._salario += self._salario * 0.12
        
if __name__ == '__main__':
    gerente = Gerente('Rodrigo', '10/01/2006', '111.222.333-44', 7.789, 1000)
    designer = Designer('Márcio', '07/05/2001', '333.444.555-66', 5.478)
    print(gerente.salario)
    gerente.get_bonificacao()
    print(gerente.salario)
        

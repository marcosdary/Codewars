# Crie três classes: Veiculo, Terrestre e Aquatico. A classe Veiculo deve ter um método deslocar() que imprime "Deslocando-se". 
# As classes Terrestre e Aquatico devem herdar de Veiculo e 
# cada uma deve ter um método tipo_deslocamento() que imprime "Deslocamento Terrestre" e "Deslocamento Aquático", respectivamente. 
# Por fim, crie uma classe CarroAnfibio que herda de ambas Terrestre e Aquatico e implementa um método usar(), que imprime "Usando veículo anfíbio".

class Veiculo:
    def deslocar(self):
        print("Deslocando-se")
        

class Terrestre(Veiculo):
    def tipo_deslocamento(self):
        print('Deslocamento Terrestre')
        
class Aquatico(Veiculo):
    def tipo_deslocamento(self):
        print('Deslocamento Aquático')
        
class CarroAnfibio(Terrestre, Aquatico):
    def usar(self):
        print("Usando veículo anfíbio")


# Crie duas classes: Animal e Voador. A classe Animal deve ter um método som() que imprime "Emitindo som". A classe Voador deve ter um método voar() 
# que imprime "Voando". Em seguida, crie uma classe Passaro que herda de ambas Animal e Voador e implementa um método descricao(), que imprime "Sou um pássaro!".
    
class Animal:
    def som(self):
        print("Emitindo som")

class Voador:
    def voar(self):
        print('Voando')
        
class Passaro(Animal, Voador):
    def descricao(self):
        print("Sou um pássaro!")
        
# Defina três classes: Pessoa, Empregado e Estudante. A classe Pessoa deve ter um método nome() que retorna o nome da pessoa. 
# Empregado deve herdar de Pessoa e ter um método cargo() que retorna o cargo do empregado. 
# Estudante deve herdar de Pessoa e ter um método curso() que retorna o curso do estudante. Por fim, crie uma classe AlunoEmpregado 
# que herda tanto de Empregado quanto de Estudante e implementa um método status(), que retorna uma mensagem indicando se a pessoa é "Aluno e Empregado" ou não.

class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    
    def nome(self):
        return self.nome
        
class Empregado(Pessoa):
    def __init__(self, nome, cargo) -> None:
        super().__init__(nome)
        self.cargo = cargo
        
    
    def cargo(self):
        return self.cargo
        
class Estudante(Pessoa):
    def __init__(self, nome, curso) -> None:
        super().__init__(nome)
        self.curso = curso
    
    def curso(self):
        return self.curso
    
   
class AlunoEmpregado(Estudante, Empregado):
    
    def __init__(self, nome, cargo, curso) -> None:
        Estudante.__init__(nome, curso)
        Empregado.__init__(nome, cargo)
        
    def status(self):
        if isinstance(self, AlunoEmpregado):
            return "Aluno e Empregado"
        else:
            return "Não é Aluno e Empregado"
        
# Exemplo de uso:
pessoa1 = AlunoEmpregado("João", "Analista de Dados", "Engenharia")
print(pessoa1.nome())  # Saída: João
print(pessoa1.cargo())  # Saída: Analista de Dados
print(pessoa1.curso())  # Saída: Engenharia
print(pessoa1.status())  # Saída: Aluno e Empregado


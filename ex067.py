# Criação de Gerenciamento de Biblioteca
from abc import ABC, abstractmethod
import datetime

# Exceções
class MenorDeIdadeException(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg        
    def __str__(self) -> str:
        return self.msg
    
class LivroNaoEncontradoError(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg        
    def __str__(self) -> str:
        return self.msg

# Livro
class Livro:
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, titulo, editora, genero) -> None:
        self.titulo = titulo
        self.editora = editora
        self.genero = genero
        self.disponivel = True
        
    def __repr__(self) -> str:
        name_class = type(self).__name__
        return f'{name_class}(nome = {self.titulo}, editora = {self.editora}, genero = {self.genero})'

# Pessoa   
class Pessoa(ABC):

    def __init__(self, nome, data_nascimento, cpf) -> None:
        self.nome = nome 
        self.data_nascimento = self.is_date(data_nascimento)
        self.cpf = cpf

    @abstractmethod
    def is_date(self, data_nascimento): ...
            
    
# Cliente
class Cliente(Pessoa):

    def __init__(self, nome, data_nascimento, cpf, email, telefone) -> None:
        super().__init__(nome, data_nascimento, cpf)
        self.email = email
        self.telefone = telefone
        self.livros = []
        self.disponivel_para_outro_livro = True

    def adicionar_livro(self, livro):
        if self.disponivel_para_outro_livro and livro.disponivel:
            self.livros.append(livro)
            livro.disponivel = False
            return True
        return False
    
    def is_date(self, data_nascimento):
        calculo = datetime.date.today() - datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        idade = int(calculo.days/365)
        if idade < 18:
            raise MenorDeIdadeException(f"{self.nome} não está na maioridade")
        return data_nascimento
        

    def remover_livro(self, nome_livro):
        livros = [l.titulo for l in self.livros]
        if nome_livro in livros:
            index = livros.index(nome_livro)
            del self.livros[index]
            return True
        raise LivroNaoEncontradoError(f'{nome_livro.titulo} específico não encontrado')
    
    def is_multa(self):
        self.disponivel_para_outro_livro = False

    def listar(self):
        texto = f'{"Título":<50} {"Editora":<30} {"Gênero"}'
        texto += '\n'
        if self.livros != []:
            for livro in self.livros:
                texto += f'{livro.titulo:<50} {livro.editora:<30} {livro.genero}\n'
        return texto

    def __repr__(self) -> str:
        name_class = type(self).__name__
        return f'{name_class}(nome = {self.nome}, data_nascimento = {self.data_nascimento}, cpf = {self.cpf}, email = {self.email}, telefone = {self.telefone}, livros = {self.livros})'
    
livro = Livro('Orgulho e Preconceito', 'Clássicos da Penguin', 'Romance, Comentário Social')
livro2 = Livro('Para Matar um Mockingbird', 'HarperCollins', ' Maioridade, Injustiça Racial')
livro3 = Livro('O Senhor dos Anéis: A Sociedade do Anel', 'Editora Record', 'Fantasia, Aventura')
livro4 = Livro('O Hobbit', 'Editora Martins Fontes', 'Fantasia, Aventura')
livro5 = Livro('Harry Potter e a Pedra Filosofal', 'Editora Rocco', 'Fantasia, Young Adult')
livro6 = Livro('Cem Anos de Solidão', 'Editora Record', 'Realismo Mágico, Literatura Latino-Americana')
livro7 = Livro('Sapiens: Uma Breve História da Humanidade', 'Editora L&PM Editores', 'História, Antropologia')
livro8 = Livro('O Caçador de Estrelas', 'Editora Objetiva', 'Romance, Ficção Científica')
livro9 = Livro('O Pequeno Príncipe', 'Editora Editora Sextante', 'Literatura Infantil, Fantasia')

cliente1 = Cliente(
    nome="Maria Silva",
    data_nascimento="1980-01-01",
    cpf="000.000.000-00",
    email="maria.silva@email.com",
    telefone="+55 (11) 9999-9999"
)

cliente2 = Cliente(
    nome="João Oliveira",
    data_nascimento="1990-02-02",
    cpf="111.111.111-11",
    email="joao.oliveira@email.com",
    telefone="+55 (12) 8888-8888"
)

cliente3 = Cliente(
    nome="Ana Souza",
    data_nascimento="2000-03-03",
    cpf="222.222.222-22",
    email="ana.souza@email.com",
    telefone="+55 (13) 7777-7777"
)

cliente4 = Cliente(
    nome="Pedro Santos",
    data_nascimento="2004-04-04",
    cpf="333.333.333-33",
    email="pedro.santos@email.com",
    telefone="+55 (14) 6666-6666"
)

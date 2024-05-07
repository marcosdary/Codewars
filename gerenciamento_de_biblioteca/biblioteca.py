class Biblioteca:
    
    def __init__(self, nome, endereco) -> None:
        
        self.nome = nome
        self.endereco = endereco
        self.lista_disponiveis = []
    
    def adicionar_livro(self, livro):
        
        if livro.disponibilidade is True:
            self.lista_disponiveis.append(livro)
            
    def listar_livros_disponiveis(self):
        
        text = ''
        text += f'Biblioteca: {self.nome}\n\n'
        
        if self.lista_disponiveis == []:
            return f'{text}\tNão há nenhum livro'
        
        for livro in self.lista_disponiveis:
            text += f'\tTítulo do livro: {livro.titulo}\n\tAutor: {livro.autor}\n\tAno de Publicação: {livro.ano_publicacao}\n\tDisponibilidade: {'Disponível'}\n'
            text += '\n'
        
        return text
    
class Livro:
    
    def __init__(self, titulo, autor, ano_publicacao) -> None:
        
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self._disponibilidade = True
        
    @property
    def disponibilidade(self):
        
        return self._disponibilidade
        
    def status(self):
        
        if self._disponibilidade:
            self._disponibilidade = False
            
        else:
            self._disponibilidade = True   
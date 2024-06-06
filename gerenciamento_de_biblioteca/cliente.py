from pessoa import Pessoa

class Cliente(Pessoa):
    
    def __init__(self, nome, idade, numero_identificacao) -> None:
        
        self.numero_identificacao= numero_identificacao
        super().__init__(nome, idade)
        self.lista_livros_emprestados = []
        
    def inserir_livro(self, livro):
        
        livro.status()
        self.lista_livros_emprestados.append(livro)
        
    def remover_livro(self, livro):
        
        if livro in self.lista_livros_emprestados:
            livro.status()
            self.lista_livros_emprestados.remove(livro)
            
            return 'Sucesso'
        raise TypeError("Livro não encontrado")
        
    def listar_livros(self):
        text = ''
        text += f'Nome do Cliente: {self.nome}\nID: {self.numero_identificacao}\n'
        
        if self.lista_livros_emprestados == []:
            return 'Não há nenhum livro'
        
        for livro in self.lista_livros_emprestados:
            
            text += f'\tTítulo do livro: {livro.titulo}\n\tAutor: {livro.autor}\n\tAno de Publicação: {livro.ano_publicacao}'
            text += ''
            
        return text 
    
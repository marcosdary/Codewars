def is_alpha_with_spaces(s:str):
    return all(c.isalpha() or c.isspace() for c in s) 
class Livro:
    def __init__(self):
        self._titulo = None
        self._autor = None

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, nome:str):
        if is_alpha_with_spaces(nome):
            self._titulo = nome

    @property
    def autor(self):
        return self._autor  # Corrigido aqui
    
    @autor.setter
    def autor(self, nome:str):
        if is_alpha_with_spaces(nome):
            self._autor = nome
            


class Biblioteca:
    def __init__(self, nome_biblioteca) -> None:
        self.nome_biblioteca = nome_biblioteca
        self.livros = []
        
    def inserir_livros(self, *livro):
        self.livros.extend(livro) if None not in livro else print("Não identificamos nenhum valor")
        
    def listar_livros(self):
        for livro in self.livros:
            if livro.titulo is not None and livro.autor is not None:
                print(f"{livro.titulo:<25}{livro.autor}")
            
from biblioteca import Biblioteca, Livro
from cliente import Cliente
from funcionario import Funcionario
        
biblioteca = Biblioteca('Conhecimento e Sabedoria', 'Rua passos')

livro_1 = Livro('Quem é você, Alaska?', 'Jhon Green', '2014')
livro_2 = Livro('Arte da Guerra', 'Xi Chaun Hi', '2021')
livro_3 = Livro('Dário, O Grande', 'Chasen', '2015')
livro_4 = Livro('Notoridade', 'Xi Chaun Hi', '2021')


cliente_1 = Cliente('Marcos', 21, '4789')
cliente_1.inserir_livro(livro_2)
cliente_2 = Cliente('Caio', 18, '4788')
cliente_2.inserir_livro(livro_3)


biblioteca.adicionar_livro(livro_1)
biblioteca.adicionar_livro(livro_2)
biblioteca.adicionar_livro(livro_3)
biblioteca.adicionar_livro(livro_4)


funcionario = Funcionario('Fernando', 27, 'Repositor')
funcionario.senha_acesso('Marcos123')

print(biblioteca.listar_livros_disponiveis())


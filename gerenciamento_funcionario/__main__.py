from departamento import Departamento
from funcionario import Vendedor, Gerente, Tecnico

vendedor = Vendedor("João Silva", "123.456.789-00", 2_000, "2020-01-01", 20_000, 0.04)

tecnico = Tecnico("Pedro Souza", "987.654.321-00", 4_500, "2022-05-15", "TI", ['Programação Java', 'Python', 'SQL', 'HTML', 'CSS', 'Javascript'])

departamento = Departamento("Vendas", "475GG", [vendedor, tecnico])

gerente = Gerente("Carlos Santos", "777.888.999-00", 6_500, "2021-03-01", departamento, [vendedor, tecnico])

departamento.adicionar_funcionario(gerente)
print(gerente.salario)
print(departamento.buscar_funcionario(vendedor))
print(tecnico.habilidade_tecnicas)
tecnico.atualizacao_tecnica("C++")
print(tecnico.habilidade_tecnicas)
print(tecnico.area_atuacao)


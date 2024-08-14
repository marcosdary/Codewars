from dataclasses import dataclass
import os

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
FOLDER = os.path.join(DESKTOP, 'Autoconsciência', 'Individuo', 'relatório salário')

@dataclass
class Funcionario:
    id_funcionario: int
    nome: str
    cargo: str
    salario: float
    data_admissao: str
  
class OperacaoFuncionarios:

    def __init__(self, funcionarios:list[dict]) -> None:
        self.funcionarios = funcionarios

    def excluir(self, id_funcionario) -> bool:
        for indice, funcionario in enumerate(self.funcionarios):
            if funcionario['id_funcionario'] == id_funcionario:
                self.funcionarios.pop(indice)
                return True
        return False
    
    def atualizar(self, campo:str, dado) -> bool | KeyError:
        try:
            self.funcionarios[campo] = dado
            return True
        except KeyError as err:
            return f'{err.__class__.__name__}: campo não encontrado'

    def remunerar(self) -> None:

        salarios = []
        salarios.append(f'{"Nome":<30} {"Salário (R$)":>10}\n')
        for funcionario in sorted(self.funcionarios, key=lambda a: a['salario']):
            salarios.append("{:<30} {:>10.2f}\n".format(funcionario["nome"], funcionario["salario"]))

        texto = ''.join(salarios)
        return texto

        

dados = [
    {
      "id": 1,
      "nome": "Ana Silva",
      "cargo": "Desenvolvedora Backend",
      "salario": 7000.00,
      "data_admissao": "2020-02-15"
    },
    {
      "id": 2,
      "nome": "Carlos Pereira",
      "cargo": "Designer Gráfico",
      "salario": 5500.00,
      "data_admissao": "2019-08-01"
    },
    {
      "id": 3,
      "nome": "Mariana Souza",
      "cargo": "Gerente de Projetos",
      "salario": 9000.00,
      "data_admissao": "2018-11-25"
    },
    {
      "id": 4,
      "nome": "Roberto Lima",
      "cargo": "Analista de Marketing",
      "salario": 6000.00,
      "data_admissao": "2021-06-10"
    }
]

operacao_funcionarios = OperacaoFuncionarios(dados)

print(operacao_funcionarios.remunerar())







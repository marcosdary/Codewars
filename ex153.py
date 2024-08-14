from json import load, dump
import os
from typing import TypedDict

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
FOLDER = os.path.join(DESKTOP, 'Autoconsciência', 'Individuo', 'empresa.json')
RELATORIO_PROJETO_CONCLUIDO = os.path.join(DESKTOP, 'Autoconsciência', 'Individuo', 'relatorio_projetos_concluidos.json')
class Funcionario(TypedDict):
    nome: str
    departamento: str
    projetos: list[dict]


with open(FOLDER, 'r', encoding='utf8') as file:
    funcionarios = load(file)['funcionarios']

projetos_concluidos = []
for funcionario in funcionarios:
    funcionario:Funcionario = funcionario
    if funcionario['projetos']:
        for projeto in funcionario['projetos']:
                projetos = {}
                if projeto['status'] == 'Concluído':
                    projetos['nome'] = funcionario['nome']
                    projetos['departamento'] = funcionario['departamento']
                    projetos['projeto'] = projeto['nome']
                    projetos_concluidos.append(projetos)

with open(RELATORIO_PROJETO_CONCLUIDO, 'w', encoding='utf8') as file:
    dump(projetos_concluidos, file, ensure_ascii=False, indent=4)

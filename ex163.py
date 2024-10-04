# Importação da base de dados para o script
from pathlib import Path
from csv import DictReader
CONTATOS = Path.home() / 'Desktop' / 'Tendencias de mercado' / 'contatos - contatos.csv'
with open(CONTATOS, 'r', encoding='utf-8') as file:
    ctts = list(DictReader(file))

# Adicionar Contato: Adicionar um novo contato ao arquivo CSV.
print("Dados do novo cliente")
nome = input("Nome: ")
email = input('Email: ')
telefone = input('Telefone: ')

# Listar Contatos: Exibir todos os contatos armazenados.
print(f"{'Nome':<20} {"Telefone":<20} {"Email"}")
for ctt in ctts:
    print(f"{ctt['Nome']:<20} {ctt['Telefone']:<20} {ctt['Email']}")
print()
# Buscar Contato: Procurar um contato específico pelo nome.
nome = input("Nome que deseja procurar: ")
for ctt in ctts: 
    if nome == ctt['Nome']:
        print(f"Olá {ctt['Nome']}, seu contato e email são respectivamente, {ctt['Telefone']} e {ctt['Email']}")
# Atualizar Contato: Editar as informações de um contato existente.
nome = input("Nome que deseja atualizar os dados: ")
for ctt in ctts: 
    if nome == ctt['Nome']:
        ctt['Nome'] = input("Nome: ")
        ctt['Email'] = input('Email: ')
        ctt['Telefone'] = input('Telefone: ')

# Excluir Contato: Remover um contato do arquivo CSV.
for index, ctt in enumerate(ctts): 
    if nome == ctt['Nome']:
        ctts.pop(index)
        break

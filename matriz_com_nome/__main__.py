import os 
import json

LOCAL_FILE = os.path.dirname(__file__)
FILE = os.path.join(LOCAL_FILE, "nomes.json")

def to_write_json(lista):
    with open(FILE, 'w', encoding='utf-8') as file:
        json.dump(lista, file, ensure_ascii=False, indent=4)
        
def read_json(lista):
    try:
        with open(FILE, 'r', encoding='utf-8') as file:
            lista_json = json.load(file)
        return lista_json
    except FileNotFoundError:
        to_write_json(lista)
    
    return lista

def existir_nome(nome_inserido):
    for indice, nome in enumerate(nomes):
        if nome['nome'] == nome_inserido:
            return f'\tHá nome na lista de nomes\n\tNo índice {indice}'
    return 'Nome não encontrado'
        
nomes = read_json([])
class Pessoa:
    
    def __init__(self, nome) -> None:
        self.nome = nome
        
        
print("\tNOMES EM UM LISTA")   
print("-="*15)
while True:
    
    nome = Pessoa(input("Digite seu nome: "))
    if sair == 's':
        print("\tFlw...")
        break
    sair = input('Para sair digite "s": ')
    nomes.append(nome.__dict__)
    to_write_json(nomes)
    
    
    
print("=-"*15)

nome_escolhido = input("Insira o nome que deseja encontrar: ")
print(existir_nome(nome_escolhido))
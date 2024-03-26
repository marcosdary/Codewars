# Lista telefônica
import os
import json

LOCAL_FILE = os.path.dirname(__file__)
ARQUIVO_JSON = os.path.join(LOCAL_FILE, "lista_telefonica_json.json")

def ler_json(lista_json_read):
    
    try:
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as file:
            lista_json_read = json.load(file)
        return lista_json_read
    except FileNotFoundError:
        escrever_json(lista_json_read)
    
   
def escrever_json(lista_json):
    with open(ARQUIVO_JSON, 'w', encoding='utf-8') as file:
        json.dump(lista_json, file, indent=4, ensure_ascii=False)

    
list_contato = ler_json([])

def validar_numero_telefonico(telefone:str):
    numero_telefonico = telefone.replace(" ", "")
    if len(numero_telefonico) == 11:
        return "({}) {}-{}".format(numero_telefonico[:2], numero_telefonico[2:7], numero_telefonico[7:])
    elif len(numero_telefonico) == 10:
        return "({}) {}-{}".format(numero_telefonico[:2], numero_telefonico[2:6], numero_telefonico[6:])
    return ValueError("Número de telefone inválido.")


def adicionar_contato(lista):
    contato = {}
    try:
        numero_identificador = int(input("Número identificado: ")) 
        nome = input("Nome: ").capitalize()
        sobrenome = input("Sobrenome: ").capitalize()
        telefone = input("Número de telefone: ").replace(" ", "")
        telefone_formato = validar_numero_telefonico(telefone)
        email = input("Email: ")
        contato["id"], contato["nome"], contato["sobrenome"], contato["telefone"], contato['email'] = numero_identificador, nome, sobrenome, telefone_formato, email
        
        lista.append(contato)
    except ValueError:
        print("\n\t\tValor inválido")
    
def exibir_lista_telefonica(lista_telefonica):
    print(f"{"ID":<20} {"NOME":<20} {"TELEFONE":<20} {"EMAIL"}")
    for telefone in lista_telefonica:
        nome_completo = f'{telefone['nome']} {telefone['sobrenome']}'
        print(f"{telefone['id']:<20} {nome_completo:<20} {telefone['telefone']:<20} {telefone['email']}")
    
    
def exibir_contato(lista_telefonica):
    nome_contato = input('nome do contato: ')
    sobrenome_contato = input("sobrenome: ")
    dados_contato = filter(lambda contato: contato['nome'] == nome_contato or contato['sobrenome'] == sobrenome_contato, lista_telefonica)
    for dado in dados_contato:
        print(f'{dado['nome']} {dado['sobrenome']} {dado['telefone']}')


def remover_contato(lista_telefonica):
    try:
        id_contato = int(input('ID do contato: '))
        for item in lista_telefonica:
            if item['id'] == id_contato:
                lista_telefonica.remove(item)
    except ValueError:
        print("\t\tID inválido")

while True:
    opcao = input("""
    ===========================================
                1. ADICIONAR CONTATO
                2. LISTAR CONTATO
                3. REMOVER CONTATO
                4. BUSCAR
                5. LIMPAR TELA
                6. SAIR          
    ===========================================
    
    Opção: """)
   
    try:
        if opcao == '6': break 
        operacao_atribuida = {
            "1": lambda: adicionar_contato(list_contato), "2": lambda: exibir_lista_telefonica(list_contato), 
            '3': lambda: remover_contato(list_contato), '4': lambda: exibir_contato(list_contato),
            '5': lambda: os.system('cls')
            }  
        operacao_atribuida.get(opcao, lambda: print("\n\t\tEscreva uma das opções disponíveis."))()
        escrever_json(list_contato)
    except TypeError:
        print("\n\t\tEscreva um das opções disponíveis")
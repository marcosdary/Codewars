import os
import json

LOCAL_FILE = os.path.dirname(__file__)
ARQUIVO_JSON = os.path.join(LOCAL_FILE, "salario_empregado.json")

def ler_json(lista_json_read):
    
    try:
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as file:
            lista_json_read = json.load(file)
        return lista_json_read
    except FileNotFoundError:
        escrever_json(lista_json_read)
    return lista_json_read    
   
def escrever_json(lista_json):
    with open(ARQUIVO_JSON, 'w', encoding='utf-8') as file:
        json.dump(lista_json, file, indent=4, ensure_ascii=False)
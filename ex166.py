from sys import argv
from os import path

print(f"Nome do script: {argv}") 

if len(argv) > 1:
    print(f"Argumentos fornecidos: {argv[1:]}")
else:
    print("nenhum argumento fornecido")


from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-n', '--name',
    help='É necessário inserir um nome',
    action='append',
    required=True
)

parser.add_argument(
    '--number',
    help='É necessário inserir um número inteiro',
    type=int, 
    nargs='+'
)

parser.add_argument(
    '--age',
    help='É necessário inserir a idade',
    type=int, 
)

parser.add_argument(
    '-v', '--verbose',
    help='É opcional',
    action='store_true'
)

parser.add_argument(
    '-i', '--item',
    help='É necessário inserir um item',
    type=str,   
    nargs='+'
)

args = parser.parse_args()
print("Processando os nomes...")
for nome in args.name:
    print(f"Olá, {nome}! Você tem {args.age} anos.")
print(f"Números fornecidos: {args.number}")
print(f"Itens fornecidos: {args.item}")
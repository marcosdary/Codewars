from argparse import ArgumentParser
from requests import get, RequestException

def consultar_cep(cep:str):
    cep = cep.replace('-', '')
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = get(url)
        response.raise_for_status()

        dados = response.json()

        if 'erro' in dados:
            print('CEP não encontrado')
         
        else:
            print(f"Endereço: {dados['logradouro']}, {dados['bairro']}, {dados['localidade']}, {dados['uf']}")
    except RequestException as e:
        print(f"Ocorreu um erro: Informações enviadas não foram encontradas pelo servidor")
    
parser = ArgumentParser()

parser.add_argument(
    "--cep",
    help="Informe o CEP a ser consultado.",
    metavar='STRING',
    type=str
)

if __name__ == "__main__":
    arg = parser.parse_args()
    if arg.cep is None:
        print("Informe o CEP a ser consultado.")

    else:
        consultar_cep(arg.cep)

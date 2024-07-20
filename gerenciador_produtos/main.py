from dataclasses import dataclass, field
import json
from os import path, system
from contextlib import contextmanager


CAMINHO = path.dirname(__file__)
ARQUIVO_JSON = path.join(CAMINHO, 'gerenciador_de_produtos.json')


@contextmanager
def Open(caminho = ARQUIVO_JSON, operacao = None):
    file = open(caminho, operacao, encoding='utf-8') 
    try:
        yield file
    except Exception as err:
        print(f'ERROR: {err}')
    finally:
        file.close()

class Json:

    def write_file(self, lista_produtos: list) -> None:
        with Open(operacao='w') as file:
            json.dump(lista_produtos, file, indent=4, ensure_ascii=False)

    def read_file(self, lista_produtos:list) -> list:
        try:
            with Open(operacao='r') as file:
                lista_produtos = json.load(file)
            
            return lista_produtos
        except FileNotFoundError:
            self.write_file(lista_produtos)
            return lista_produtos
leitura = Json().read_file([])
escrita = Json().write_file

counter = 0 if leitura == [] else max(leitura, key=lambda k: k['id_'])['id_']

def generate_id() -> int:
    global counter
    counter += 1    
    return counter

@dataclass
class Produto:
    nome: str
    validade: str
    preco: float
    quantidade: int
    id_:int = field(default_factory=generate_id)  

@dataclass(frozen=True)
class Gerenciador:
    produtos: list[Produto] = field(default_factory=list)
    def exibir(self) -> str:
    
        texto = ''
        texto += f'''
                {"ID":<20} {"NOME":<40} {"VALIDADE":<20} {"PREÇO (R$)"}
            '''
        
        for item in self.produtos:
            texto += f'''
                {item["id_"]:<20} {item["nome"]:<40} {item["validade"]:<20} {item["preco"]}
            '''
        
        return texto

    def remover_produto(self, id_:int) -> str:
        for i, item in enumerate(self.produtos):
            if id_ == item['id_']:
                self.produtos.pop(i)
                return 'REMOÇÃO DO PRODUTO BEM SUCEDIDO :-D'
        return 'PRODUTO NÃO ENCONTRADO :('
    
    def atualizar_produto(self, id_:int) -> Produto:
        for item in self.produtos:
            if id_ == item['id_']:
                return item
        raise TypeError(f'Objeto não encontrado com id: {id_}')

class OperacoesInterface:

    @staticmethod
    def novo_produto():
        while True:
            try:
                print(
                '''
                               - DADOS DO PRODUTO -
                ''')
                nome = input(
                        '''
                                 Nome do produto
                            - '''
                )
                data_validade = input(
                        '''
                            Data de Validade DD/MM/AAAA
                            - '''
                )
                preco = input('''
                                   Preço (R$)
                            - '''
                )
                quantidade = input('''
                                   Quantidade
                            - '''
                )
                produto = Produto(nome=nome, validade=data_validade, preco=preco, quantidade=quantidade)
                if leitura is not None:    
                    leitura.append(produto.__dict__)
                    return leitura
            except ValueError as err:

                print(
                    f'''
                            ESCREVA NOVAMENTE ):
                    '''
                )
    
    @staticmethod
    def atualizar_produto():
        while True:
            id_produto = input(
                '''
                               ID do Produto: 
                            - '''
            )
            try:
                produto = Gerenciador(leitura).atualizar_produto(int(id_produto))
                print(
                    '''
                        ----------------------------------------------------
                        1.                                              NOME
                        2.                                             PREÇO
                        3.                                          VALIDADE
                        4.                                        QUANTIDADE
                        ----------------------------------------------------
                    '''
                )
                opcao = input(
                    '''
                        Opção: 
                    '''
                )
                    
                print(
                    '''
                        -------------------- ATUALIZAÇÃO --------------------
                    '''
                )
                match opcao:
                    case '1':
                        nome = input(
                            '''
                                             Novo nome
                                    - '''
                        )
                        produto['nome'] = nome
                        return leitura
                    case '2':
                        preco = float(input(
                            '''
                                            Novo preço 
                                    - '''
                        ))
                        produto['preco'] = preco                            
                        return leitura
                    case '3':
                        validade = int(input(
                            '''
                                            Nova validade
                                    - '''
                        ))
                        produto['validade'] = validade
                        return leitura
                    case '4':
                        quantidade = int(input('''
                                            Nova quantidade 
                                    - '''
                        ))
                        produto['quantidade'] = quantidade
                        return leitura
                    case _:
                        print(
                        '''
                                    OPÇÃO INVÁLIDA ):
                        '''
                        )

            except TypeError:
                print(
                    '''
                                ESCREVA NOVAMENTE ID ):
                    '''
                )
            except ValueError:
                print(
                    '''
                                DADOS INVÁLIDOS, CORRIGIA-OS
                    '''
                )

    @staticmethod
    def remover_produto():
        while True:
            id_produto = input(
                '''
                            ID do Produto 
                        - '''
                )
            try:
                    print(
                        f'''
                            {Gerenciador(leitura).remover_produto(int(id_produto))}

                        '''
                    )
                    return leitura 
            except TypeError:
                print(
                    '''
                        ESCREVA NOVAMENTE ID ):
                    '''
                    )
while True:
    print(
        '''
            ==================================================================
            1.                                                    NOVO PRODUTO
            2.                                               ATUALIZAR PRODUTO
            3.                                        EXIBIR TODOS OS PRODUTOS
            4.                                                 REMOVER PRODUTO
            5.                                                            SAIR
            6.                                                      LIMPA TELA
            ==================================================================
        '''
    )
    opcao = input('             Opção: ')
    operacao = OperacoesInterface()
    match opcao:
        
        case '1':
            print(
            '''
            -------------------------------------------------------------------
            '''
            )
            escrita(operacao.novo_produto())
            print(
            '''
                        PRODUTO ADICIONADO COM SUCESSO :)^_____^
            -------------------------------------------------------------------
            '''
            )
        case '2':
            escrita(operacao.atualizar_produto())
            print(
            '''
                ALTERAÇÃO SOBRE O PRODUTO REALIZADO COM SUCESSO :-) ^_~

            '''
            )
        case '3':
            system('cls')
            print(Gerenciador(leitura).exibir())
            
        case '4':
            escrita(operacao.remover_produto())
        case '5':
            print(
            '''
                OBRIGADO PELA ATENÇÃO, VOLTE SEMPRE :-D ^_~
            
            '''
            )
            break
        case '6':
            system('cls')

        case _:
            print(
            '''
                ESCOLHA UMA DAS OPÇÕES :-D
            '''
            )


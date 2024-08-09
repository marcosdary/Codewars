# Criando uma estrutura de diretórios:
# Crie um diretório principal chamado "projeto".
# Dentro de "projeto", crie subdiretórios "dados", "scripts" e "resultados".
# Dentro de "dados", crie subdiretórios "brutos" e "processados" 

import os
import shutil


HOME = os.path.expanduser("~")
DESKTOP = os.path.join(HOME, 'Desktop')
PROJETO = os.path.join(DESKTOP, 'Projeto')

# Crie um arquivo chamado "arquivo_antigo.txt" 
# dentro do diretório "dados/brutos".
# Renomeie o arquivo para "arquivo_novo.csv".

BRUTOS = os.path.join(PROJETO, 'dados\\brutos')
arquivo_novo = os.path.join(BRUTOS, 'arquivo_novo.txt')
arquivo_novo_csv = os.path.join(BRUTOS, 'arquivo_novo.csv')

# Exclua o arquivo "arquivo_novo.csv" que você acabou de criar.
# Exclua o diretório "resultados" e todo o seu conteúdo (se existir)

# os.unlink(arquivo_novo_csv)
RESULTADO = os.path.join(PROJETO, 'resultados')
shutil.rmtree(RESULTADO, ignore_errors=True)

# Crie 10 arquivos aleatórios dentro do diretório "dados/brutos".
# Mova todos os arquivos com a extensão ".txt" para um novo diretório chamado "textos".
# Mova todos os arquivos com a extensão ".csv" para um novo diretório chamado "csv"



dados = [
    {
        'extensao':'gastoviagem.txt',
        'texto':
            '''
            Data,Descrição,Categoria,Valor(R$)
            01/01/2024,Hospedagem,Alojamento,500.00
            02/01/2024,Transporte,Transporte,200.00
            03/01/2024,Alimentação,Alimentação,150.00
            '''
    },
    {
        'extensao': 'vendasloja.txt',
        'texto':
            '''
            Data da Venda,Produto,Quantidade,Valor Total
            01/01/2024,Camiseta,2,50.00
            02/01/2024,Calça,1,100.00
            '''
    },
    {
        'extensao': 'tarefaprojeto.txt',
        'texto':
            '''
            Tarefa,Responsável,Data de Início,Data de Término,Status
            Desenvolver o layout,João,01/01/2024,15/01/2024,Em andamento
            Criar a base de dados,Maria,05/01/2024,31/01/2024,Concluído
            '''
    },
    {
        'extensao': 'gastopessoais.txt',
        'texto':
            '''
            Data,Descrição,Categoria,Valor(R$)
            01/01/2024,Almoço,Alimentação,30.00
            02/01/2024,Transporte,Transporte,10.00
            03/01/2024,Conta de luz,Casa,120.00
            '''
    },
    {
        'extensao': 'gastocarro.txt',
        'texto':
            '''
            Data,Descrição,Categoria,Valor(R$)
            01/01/2024,Combustível,Manutenção,100.00
            05/01/2024,Troca de óleo,Manutenção,250.00
            10/01/2024,Estacionamento,Outros,50.00
            '''
    },
    {
        'extensao': 'clientes.txt',
        'texto':
            '''
            Código,Nome do Cliente,Valor da Compra
            1001,João da Silva,500.00
            1002,Maria Oliveira,250.50
            1003,Pedro Souza,789.99
            '''
    },
    {
        'extensao': 'evento.txt',
        'texto':
            '''
            Nome do Evento,Data do Evento,Local,Número de Participantes
            Conferência de Tecnologia,15/03/2024,Centro de Convenções,500
            Workshop de Marketing,20/04/2024,Hotel XYZ,100
            '''
    },
    {
        'extensao': 'registroproduto.txt',
        'texto':
            '''
            Código do Produto,Nome do Produto,Descrição,Preço,Quantidade em Estoque
            PROD001,Camiseta Preta,Camiseta básica de algodão,29.99,100
            PROD002,Calça Jeans,Calça jeans skinny,99.90,50
            '''
    },
    {
        'extensao': 'dadosblog.txt',
        'texto':
            '''
            Título do Post,Data de Publicação,Categoria,Número de Visualizações
            Como criar um CSV,15/03/2024,Tutoriais,200
            As melhores ferramentas para edição de fotos,20/04/2024,Dicas,150
            '''
    }
]

TEXTO = os.path.join(PROJETO, 'textos')
os.makedirs(TEXTO, exist_ok=True)

for arquivo in os.listdir(BRUTOS):
    
    caminho_original = os.path.join(BRUTOS, arquivo)
    caminho_original = shutil.move(caminho_original, caminho_original.replace('.txt', '.csv'))
    shutil.copy(caminho_original, TEXTO)
    
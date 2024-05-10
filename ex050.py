from random import randint
class Jogador: 
    
    def __init__(self, nome) -> None:
        self._username = nome
        self.__status = False
    
    @property
    def status(self):
        return self.__status
    
    
class Adivinhar:
       
    MAXIMO_TENTATIVAS = 10
    PONTUACAO_MAXIMA = 100
    MENSAGENS_PADRAO = {
        'DEFAULT': {
                'SAUDACAO': lambda nome: f'\nOlá {nome}, a pontuação de ínicio do jogo é 100 pontos\n',
                'ENCERRAMENTO': lambda nome: f'\nQue pena {nome}, o número máximo de tentativas se encerrou...\n',
                'VITORIA': '\tParabéns!! você ganhou',
                'DERROTA': '\n\tQue pena!! você perdeu\n\tMas na próxima, irá dar certo',
                'INPUT': 'Digite um número entre 0 a 10: ',
                'NOVA_PARTIDA': 'Gostaria de jogar novamente? (1 - Sim; 2 - Não) ',
                'PONTUACAO': lambda pontuacao: f'\tA sua pontuação final é {pontuacao} pontos'
            },
        'ERROR': {
            'NUMERO_INVALIDO': lambda erro: f'\n\tStatus do erro: {erro}\n',
            'ESCOLHA_INVALIDA': f'escolha entre \n\t1 - Sim\t\t2 - Não'
        }
    }
    
    def __init__(self) -> None:
        self.inicia = self.__inicio
    
    def __inicio(self, nome_jagador):
        
        pontuacao = 100    
        i = 0
        print(self.MENSAGENS_PADRAO['DEFAULT']['SAUDACAO'](nome_jagador))
        while i < self.MAXIMO_TENTATIVAS:
    
            try:
                numero = int(input(self.MENSAGENS_PADRAO['DEFAULT']['INPUT']))
        
                if 0 <= numero <= 10:
                    numero_aleatorio = randint(0, 10)
                    
                    if numero_aleatorio != numero:
                        pontuacao -= 10  
                         
                    i += 1
                    
                else:
                    raise ValueError("deve ser entre 0 a 10")
            except ValueError as err:
                print(self.MENSAGENS_PADRAO['ERROR']['NUMERO_INVALIDO'](err))
                
        print(self.MENSAGENS_PADRAO['DEFAULT']['ENCERRAMENTO'](nome_jagador))
        print(self.MENSAGENS_PADRAO['DEFAULT']['PONTUACAO'](pontuacao))
        
        self.__fim(pontuacao)
        
    def __fim(self, pontuacao):
        while True:
        
            joga_novamente = input(self.MENSAGENS_PADRAO['DEFAULT']['NOVA_PARTIDA'])
            try:
                if joga_novamente not in ['1', '2']:
                    raise ValueError(self.MENSAGENS_PADRAO['ERROR']['ESCOLHA_INVALIDA'])
                
                if joga_novamente == '2':
                    
                    if self.PONTUACAO_MAXIMA == pontuacao:
                        print(self.MENSAGENS_PADRAO['DEFAULT']['VITORIA'])
                        return 
                    
                    else:
                        print(self.MENSAGENS_PADRAO['DEFAULT']['DERROTA'])
                        return 
                    
                return self.__inicio()
            
            except ValueError as err:
                
                print(self.MENSAGENS_PADRAO['ERROR']['NUMERO_INVALIDO'](err))
           

def executar(nome):
    
    jogador = Jogador(nome)
    jogo = Adivinhar().inicia(nome)
    

if __name__ == '__main__':
    nome_jogador = input('Qual é seu nome? ')
    executar(nome_jogador)
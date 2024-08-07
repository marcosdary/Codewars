class MovimentoUiforme:
    def __init__(self, **kwds) -> None:
        self.kwds = kwds

    def velocidade(self):
        return (self.kwds['sf'] - self.kwds['si'])/self.kwds['t']

    def posicao_final(self):
        return self.kwds['si'] + self.kwds['v'] * self.kwds['t']
    
    def tempo(self):
        return (self.kwds['sf'] - self.kwds['si']) / self.kwds['v'] 
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.kwds})' 
    
    def movimento(self):
        valor = 'Progressivo' if self.kwds['v'] > 0 else 'Regressivo'
        return 'Movimento' + valor
    
'''
Uma ave migratória consegue voar enormes distâncias. 
Suponha que ela consiga voar com velocidade constante de 
10 m/s durante o período de uma semana. Qual terá sido a 
distância, em quilômetros, percorrida pela ave durante esse período?

a) 2056 km

b) 6048 km

c) 7512 km

d) 8600 km

'''
dados = {'v': 10, 't': 24*7*3600, 'si':0}
mu = MovimentoUiforme(**dados)
print(f'Distância final igual a: {mu.posicao_final()}m')

'''
(Famema) De dentro do ônibus, que ainda fazia manobras para estacionar 
no ponto de parada, o rapaz, atrasado para o encontro com a namorada, 
a vê indo embora pela calçada. Quando finalmente o ônibus para e o rapaz 
desce, a distância que o separa da namorada é de 180 m.

Sabendo que a namorada do rapaz se movimenta com velocidade constante de 
0,5 m/s e que o rapaz pode correr com velocidade constante de 5 m/s, o 
tempo mínimo para que ele consiga alcançá-la é de:

a) 10 s.

b) 45 s.

c) 25 s.

d) 50 s.

e) 40 s.
'''

dados = {'sf': 180, 'si':0, 'v':4.5}
mu = MovimentoUiforme(**dados)
print(f'Tempo mínimo: {mu.tempo()}')

'''
Na pista de testes de uma montadora de automóveis, foram feitas medições 
do comprimento da pista e do tempo gasto por um certo veículo para percorrê-la. 
Os valores obtidos foram, respectivamente, 1030 m e 25,0 s. Levando-se em conta
a precisão das medidas efetuadas, é correto afirmar que a velocidade média desenvolvida 
pelo citado veículo foi, em m/s, de:

a) 4,10.

b) 41.

c) 41,2.

d) 41,20.

e) 41,200
'''

dados = {'sf': 1030, 'si':0, 't':25}
mu = MovimentoUiforme(**dados)
print(f'Velocidade média: {mu.velocidade()}')


'''
(Unitau) Um automóvel percorre uma estrada com função horária S = - 40 + 80t,
sendo que S é dado em km e t está em horas. O automóvel passa pelo km zero após:

a) 1,0 h.

b) 1,5 h.

c) 0,5 h.

d) 2,0 h.

e) 2,5 h.
'''

dados = {'sf': 0, 'si':-40, 'v':80}
mu = MovimentoUiforme(**dados)
print(f'Tempo: {mu.tempo()}')
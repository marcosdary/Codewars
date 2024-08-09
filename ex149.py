# Implemente a solução para o problema da mochila, onde o usuário tem uma mochila com capacidade 
# limitada e uma lista de itens, cada um com um peso e um valor. 
# O programa deve calcular o valor máximo que pode ser carregado na mochila sem exceder a capacidade

class Mochila:
    def __init__(self, carga_maxima:int) -> None:
        self.items = []
        self._carga_atual = 0
        self._carga_maxima = carga_maxima

    def adicionar_item(self, item:dict) -> bool:
        self._carga_atual += item['peso']
        
        if not self._carga_atual <= self._carga_maxima:
            raise ValueError('Acima do permitido pela bolsa')
        
        self.items.append(item)
        return True
    
    @property
    def carga_maxima(self):
        return self._carga_maxima
    
    @property
    def carga_restante(self):
        return self._carga_maxima - self._carga_atual
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}(carga_maxima={self._carga_maxima},carga_atual={self._carga_atual:.2f})'

mochila_1 = Mochila(40)

item_1 = mochila_1.adicionar_item({'item': 'camisa', 'peso':2})
item_2 = mochila_1.adicionar_item({'item': 'ursinho pooh', 'peso': 0.78})

print(mochila_1)
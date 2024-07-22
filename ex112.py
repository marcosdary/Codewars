# Crie uma classe chamada ReversedList, que implementa 
# a interface Iterable e permite iterar sobre uma lista 
# de trás para frente. A classe deve ser capaz de receber
# uma lista como entrada e retornar um iterador 
# que percorre os elementos dessa lista em ordem inversa.

# Passos:
# Defina a classe ReversedList:

# A classe deve ter um construtor que recebe uma lista como argumento.
# Implemente o método __iter__ que retorna um iterador.
# Defina a classe ReversedIterator:

# Esta classe deve ser o iterador que percorre a lista em ordem inversa.
# Implemente os métodos __iter__ e __next__.

from collections.abc import Iterable
from typing import Iterator
from random import randint

class ReversedList(Iterable):
    def __init__(self, data) -> None:
        self._data = data

    def __iter__(self) -> Iterator:
        return ReversedIterator(self._data)


class ReversedIterator:
    
    def __init__(self, data) -> None:
        self._data = data
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index <= -len(self._data):
            self._index = -1
            raise StopIteration
        
        self._index -= 1
        return self._data[self._index]
    
if __name__ == '__main__':

    lista = list(randint(10, 100) for _ in range(0, 10))
    for numero in ReversedList(lista):
        print(numero, end=' ')
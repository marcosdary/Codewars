# Crie uma classe chamada EvenNumberSequence, que implementa a interface Iterable e permite 
# iterar sobre todos os números pares em uma faixa de valores fornecida. A classe deve ser 
# capaz de receber dois números inteiros (start e end) como entrada e retornar um iterador 
# que percorre todos os números pares nessa faixa, incluindo start se for par e excluindo end.

from collections.abc import Iterable
from typing import Iterator

class EvenOrOddNumberSequence(Iterable):

    def __init__(self, start:int, end:int, even:bool = True) -> None:
        self._current = start if start % 2 == 0  and even else \
                    start + 1 if even else \
                    start + 1 if not even else start
        self._end = end

    def __iter__(self) -> Iterator:
        return self
    
    def __next__(self):
        if self._current >= self._end:
            raise StopIteration
        value = self._current
        self._current += 2    
        return value

for num in EvenOrOddNumberSequence(3, 15):
    print(num)
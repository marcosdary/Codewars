# Crie uma classe chamada PrimeNumberSequence, que implementa a interface Iterable 
# e permite iterar sobre todos os números primos em uma faixa de valores fornecida. 
# A classe deve ser capaz de receber dois números inteiros (start e end) como entrada e retornar 
# um iterador que percorre todos os números primos nessa faixa, incluindo start se for primo e excluindo end.
from collections.abc import Iterable
from typing import Iterator

def is_prime(num:int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def tuple_primes(start:int, end:int, lst:list = []):
    if start >= end:
        return lst
    if is_prime(start):
        lst.append(start)
    start += 1
    return tuple_primes(start, end, lst)

class PrimeNumberSequence(Iterable):
    
    def __init__(self, start, end) -> None:
        self._data = tuple_primes(start, end)

        self.index_next = 0
    
    def __iter__(self) -> Iterator:
        return self
    
    def __next__(self):
        if self.index_next >= len(self._data):
            print(self._data)
            raise StopIteration
        value = self._data[self.index_next]
        self.index_next += 1
        return value
        
for num in PrimeNumberSequence(0, 100):
    print(num)
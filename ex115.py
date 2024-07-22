# Crie uma classe chamada FibonacciSequence, que implementa a interface Iterable
# e permite iterar sobre os primeiros n números da sequência de Fibonacci. A classe
# deve ser capaz de receber um número inteiro n como entrada e retornar 
# um iterador que percorre os primeiros n números da sequência de Fibonacci.
from collections.abc import Iterable
from typing import Iterator

def fibonacci(number:int):

    if number in [0, 1]:
        return number
    
    return fibonacci(number-1) + fibonacci(number-2)

class FibonacciSequence(Iterable):

    def __init__(self, start, end) -> None:
        self._current = start 
        self._end = end

    def __iter__(self) -> Iterator:
        return self
    
    def __next__(self):
        if self._current >= self._end:
            raise StopIteration

        valeu = self._current
        self._current += 1
        return fibonacci(valeu)
    
for fibo in FibonacciSequence(0, 10):
    print(fibo, end=' -> ')
print('Fim')
        
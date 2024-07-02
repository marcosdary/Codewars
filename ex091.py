# Escreva uma função que, dado um array arr, retorne um array contendo em cada índice i a quantidade de números que são menores que arr[i]à direita.
# Por exemplo:
# * Input [5, 4, 3, 2, 1] => Output [4, 3, 2, 1, 0]
# * Input [1, 2, 0] => Output [1, 1, 0]
# Se você completou este e quer testar seu desempenho e ajustar este mesmo kata, vá para a versão muito mais difícil. Quantos são menores que eu II?
from functools import reduce
def smaller(arr):
    '''
    smaller arr

    This function seeks to find the number of numbers that are smaller than the current index.
    Initially, filter is used, which filters the data in the "arr" array and, subsequently, the len that adds up all "x" 
    of the loop, to parse across the array on the right to thus sum as an accumulator

    : param arr: array
    : type arr: list

    : return: sum of the number of values smaller than the current index and to the right  
    : rtype:list
    '''
    arr = list(
            map(
                lambda x: reduce(
                    lambda ac, x: ac + 1, arr, 0 
                )
            )
        )
    return arr

print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]))
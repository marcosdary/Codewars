# https://www.codewars.com/kata/628d253eb110f3270a8a1789/train/python
def determinateValue(x, y, n):

    return 0

lista = [
    [ 1,  2,  6,  7, 15],
    [ 3,  5,  8, 14, 16],
    [ 4,  9, 13, 17, 22],
    [10, 12, 18, 21, 23],
    [11, 19, 20, 24, 25]
]
for linha in lista:
    for coluna in linha:
        print(coluna, linha.index(coluna), lista.index(linha))
    print()



        
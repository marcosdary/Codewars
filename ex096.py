from collections import Counter
def find_it(seq: list) -> int | float:
    count = tuple(filter(lambda a: a[1] % 2 != 0,Counter(lista).items()))
    return max(count, key= lambda a: a[1])[0]
lista = [0,1,0,1,0] # 0
print(find_it(lista))
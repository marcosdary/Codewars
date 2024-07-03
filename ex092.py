def sort_array(source_array):
    impares = list(filter(lambda a: a % 2 != 0, source_array))
    impares.sort()
    numeros = list(filter(lambda a: a % 2 == 0, source_array))
    print(numeros)
    p = 0
    for i, a in enumerate(source_array):
        if a % 2 != 0:
            numeros.insert(i, impares[p])
            p += 1
    return numeros

print(sort_array([5, 8, 6, 3, 4]))  # [3, 8, 6, 5, 4]
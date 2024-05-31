from itertools import combinations 
def twos_difference(lst): 
    mat = []
    for c in combinations(lst, 2):
        if c[0] > c[1]:
            s = c[0] - c[1]
        else:
            s = c[1] - c[0]
        if s == 2:
            
            mat.append(tuple(sorted(c)))
    mat.sort()
    return mat

vet = [6, 3, 4, 1, 5]
print(twos_difference(vet))
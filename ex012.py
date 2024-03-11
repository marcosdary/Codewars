
def solution(array_a, array_b):
    array_c = [
    (x - y)**2
    if x >= y else (y - x)**2
    for x, y in zip(array_a, array_b)
    ]
    
    s = sum(array_c)/len(array_c)
    
    return s

a, b = [10, 20, 10, 2], [10, 25, 5, -2]
print(solution(a, b))

def solution(array_a, array_b):
    array_c = [
    (x - y)**2
    if x >= y else (y - x)**2
    for x, y in zip(array_a, array_b)
    ]
    
    d = ' + '.join(str(i) for i in array_c)
    s = f'{sum(array_c)/len(array_c)} because ({d}) / {len(array_c)}'
    
    return s
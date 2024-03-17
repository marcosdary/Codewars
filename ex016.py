def is_happy(num):
    while num != 1 and num != 4:  # 4 é o primeiro número não feliz
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1

def perf_happy(n):
    def precalculate_happy(limit, current=1, happy_set=set()):
        if current > limit:
            return happy_set
        if is_happy(current):
            happy_set.add(current)
        return precalculate_happy(limit, current + 1, happy_set)
    
    return precalculate_happy(n)

# Realizar o pré-cálculo dos números felizes até 10 milhões
happy = perf_happy(10_000_000)

# Testar a função perf_happy para os números até 100
result = perf_happy(100)
print(result)
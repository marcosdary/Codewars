def decorator(func):
    n = 0
    def inner_function(*args, **kwargs):
        nonlocal n
        n += 1
        print(f"Número de vezes que a função foi chamada: {n}")
        return func(*args, **kwargs)
    return inner_function

@decorator
def soma(a, b):
    return a + b
# Desenvolva um decorador que armazene em cache os resultados 
# de uma função para evitar cálculos repetidos.
def cache_decorator(func):
    cache = {}
    def inner_function(*args, **kwargs):
        if args in cache:
            print(f"Há no cache: {cache}")
            return cache[args]
        cache[args] = func(*args, **kwargs)
        return func(*args, **kwargs)
    return inner_function


# Crie um decorador que reexecute automaticamente uma função algumas 
# vezes em caso de exceção, com a possibilidade de definir o número máximo de tentativas.
def rerun_deco(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            tentativas = int(input("Deseja quantas tentativas: "))
            return argument_new(func, tentativas)
        except TypeError:
            tentativas = int(input("Deseja quantas tentativas: "))
            return argument_new(func, tentativas)
    return inner_function

# Interdemediário para recolocar os valores 
def argument_new(func, max_attemps = 5):
    temp = 1
    while temp < max_attemps:
        print(f"NÚMERO DE TENTATIVA: {temp}")
        try: 
            a = float(input("1° número: "))
            b = float(input("2° número: "))
            resultado = func(a, b)
            return resultado
        except ValueError:
            print("\n\tEscreva novamente os números\n")
        except ZeroDivisionError:
            print(f'\n\tImpossível calcular divisão por 0\n')
        temp += 1
    return 'FINALIZOU SUAS TENTATIVAS'
        
            

# Função para adicionar o decorador

@cache_decorator
@rerun_deco
def divisao(a, b):
    return a / b

# Testes

t1 = divisao(4, 5)
t2 = divisao(7, 8)
t3 = divisao(7, 8)

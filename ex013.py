from itertools import permutations as permutations_str

def decorator_permutations(func):
    def inner_function(*args, **kwargs):
        for arg in args:
            is_number(arg) # avaliar se há número na variável da string, caso não haja func(*args, **kwargs) será executado
        return func(*args, **kwargs)
    return inner_function

@ decorator_permutations
def permutations(s):
    permutations_string = {''.join(x) for x in list(permutations_str(s))} # Primeiro, há o permutations_str que faz todas as
    return list(permutations_string)                                      # combinações possíveis, depois ela é armazenada na lista por ser uma classe
                                                                          # Por fim, {} ou set() que inibir ter repetições nessas combinações
def is_number(string:str):
    if string.isnumeric():
        raise ValueError ("There can be no numbers") # Aqui, avaliar as entradas do usuário, caso seja a string um número, ela abrir uma exceção
                                                      # com seguinte argumento: "Não pode haver números"

word = 'aabb'  # permutations(word) ==> ['bbaa', 'abba', 'abab', 'baba', 'baab', 'aabb']                               

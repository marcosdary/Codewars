from itertools import permutations

def latest_clock(a, b, c, d):
    numbers = a, b, c, d # Aqui, os números a, b, c, d são colocados em uma tupla que recebe nome "numbers"
    permutacoes_horarios = [
        ''.join(str(i) for i in x)              # Primeiro, há todas as combinações possiveis para formar um número, para que         
        for x in list(permutations(numbers, 4)) # seja concatenado com uso do "".join(). Todavia, o join() não aceita valores do tipo int. Desse modo, houve há necessidade
    ]                                           # de ter usa str(i) junto ao loop de repetição ==> ['6024', '6042', '6204', '6240', ...]
                                                                

    filtro_horarios = list(filter(lambda x: 00 <= int(x[:2]) <= 24 and 00 <= int(x[2:]) <= 59, permutacoes_horarios)) # O uso de filter foi utilizado para atender a o HH:MM, foi pego x[:2] que pega os dois primeiro números e transforma em inteiros para ser a hora, que são 24
                                                                                                                      # já o restante, ou seja, x[2:] avaliar os minutos, que são 59 minutos 
                                                                                                                      # Os valores escolhidos para (6, 0, 2, 4) foram ['0624', '0642', '0246', '0426', '2046', '2406']
    numero_escolhido = max(filtro_horarios)  # Aqui, é pego o maior valor, como '2406'                             
    hh, mm = numero_escolhido[:2], numero_escolhido[2:] # Por fim, aqui é divido em formato HH:MM, assim como adicionado o ":"
    horario = f'{hh}:{mm}'
    return horario # 24:06



print(latest_clock(6, 0, 2, 4))

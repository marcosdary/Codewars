from itertools import permutations

def latest_clock(a, b, c, d):
    numbers = a, b, c, d
    permutacoes_horarios = [
        ''.join(str(i) for i in x)
        for x in list(permutations(numbers, 4))
    ]

    filtro_horarios = list(filter(lambda x: 00 <= int(x[:2]) <= 24 and 00 <= int(x[2:]) <= 59, permutacoes_horarios))
    numero_escolhido = max(filtro_horarios)
    hh, mm = numero_escolhido[:2], numero_escolhido[2:]
    horario = f'{hh}:{mm}'
    return horario



print(latest_clock(6, 0, 2, 4))
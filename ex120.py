from datetime import datetime
from enum import Enum

class DiaDaSemana(Enum):
    SEGUNDA = 'segunda-feira'
    TERCA = 'terça-feira'
    QUARTA = 'quarta-feira'
    QUINTA = 'quinta-feira'
    SEXTA = 'sexta-feira'
    SABADO = 'sabádo'
    DOMINGO = 'domingo'

def dia_da_semana(resultado):
    dia = DiaDaSemana
    match resultado:
        case 0:
            return dia['SEGUNDA']
        case 1:
            return dia['TERCA']
        case 2:
            return dia['QUARTA']
        case 3:
            return dia['QUINTA']
        case 4:
            return dia['SEXTA']
        case 5:
            return dia['SABADO']
        case 6:
            return dia['DOMINGO']
        case _:
            raise TypeError('Dados incorretos - refaça-o')

try:
    day = int(input('Dia: '))
    month = int(input('Mês: '))
    year = int(input('Ano: '))

    date = datetime(year, month, day)
    A = date.year // 100
    B = A // 4
    C = 2 - A + B
    D = int(365.25 * (date.year + 4716))
    E = 30.6001 * (date.month + 1)
    dia_juliano = D + E + date.day + C - 1524
    dia = int(dia_juliano % 7)

    print(f'Dia da semana: {dia_da_semana(dia).value}')
except ValueError:
    print(
        """
                Dados não estão no formato DD/MM/AAAA ou
                Valores não são inteiros
        """
    )
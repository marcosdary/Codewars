from calendar import day_name, monthcalendar, month_name
import locale
from textwrap import indent

locale.setlocale(locale.LC_ALL, 'pt_BR')
class Calendario:

    def __init__(self, dia: int, mes:int, ano:int) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.nome_dia_semana = None

    def dia_da_semana(self):
        mes = [x for semana in monthcalendar(self.ano, self.mes) for x in enumerate(semana) if x[0] != 0]
        self.nome_dia_semana = tuple(filter(lambda x: x[1] == self.dia, mes))[0][0]
        return f'{day_name[self.nome_dia_semana].capitalize()}, {month_name[self.mes]} de {self.ano}'
    
    def calendario(self):
        cal = ''
        cal += f"{"Seg":<4}{"Ter":<4}{"Qua":<4}{"Qui":<4}{"Sex":<4}{"Sab":<4}{"Dom":<4}\n"
        for semana in monthcalendar(self.ano, self.mes):
            for dia in semana:
                if dia == 0:
                    cal += f'{"X":^3} '
                else:
                    cal += f'{dia:^3} '
            cal += '\n'
        cal += '\nLEGENDA\n'
        cal += 'X: Não faz parte deste mês\n'
        return cal
agosto = Calendario(2, 8, 2024)

print(indent(agosto.calendario(), ' '*20))
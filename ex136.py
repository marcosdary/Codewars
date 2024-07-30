from calendar import day_name, weekday, month_name
import locale

locale.setlocale(locale.LC_ALL, "pt_BR")

MESES = list(month_name)[1:]
DAYS = list(day_name)

try:
    ano = int(input('Ano: '))
    mes = int(input('Mês: '))
    dia = int(input('Dia: '))
    dia_semana = weekday(year=ano, month=mes, day=dia)
    print(
        f"""
            {DAYS[dia_semana]}, {dia} de {MESES[mes-1]} de {ano}
        """
    )
except ValueError:
    print(
        '''
                Coloque os dados válidos - Inteiros
        '''
    )



# De acordo com a ISO 8601, a primeira semana do calendário 
# (1) começa com a semana que contém a primeira quinta-feira 
# de janeiro. Cada ano consiste em 52 semanas do calendário 
# (53 no caso de um ano que começa em uma quinta-feira ou 
# um ano bissexto que começa em uma quarta-feira).

# Sua tarefa é calcular a semana do calendário (1-53) de uma 
# data dada. Por exemplo, a semana do calendário para a data 
# 2019-01-01(string) deve ser 1 (int)

# get_calendar_week("2017-01-01") -> 52
from calendar import monthcalendar
from datetime import datetime, date



def get_calendar_week(date_string):
    date_string = datetime.fromisoformat(date_string)

    return date.isocalendar(date_string).week

print(get_calendar_week("2018-12-31"))
# to_industrial(time)deve aceitar o tempo em minutos como um inteiro ou uma string 
# do formato "h:mm". Minutos sempre consistirão em dois dígitos nos testes
#  (por exemplo, "0:05"); horas podem ter mais. Retorna um float que representa horas decimais 
# (por exemplo, 1,75 para 1h 45m). 
# Arredonde para uma precisão de dois dígitos decimais - não simplesmente trunque!
from datetime import datetime

def to_industrial(time:int | str) -> float:
    if isinstance(time, int):
        return round(time / 60, 2)
    
    hour, minute = time.split(':')
    print(hour, minute)
    return 

def to_normal(time):
    integer = int(time)
    decimal = round(time - integer, 2) * 60
    minute = f'{decimal % 60:.0f}'
    hours = f'{integer + decimal // 60:.0f}:{minute if len(minute) == 2 else minute + '0' if round(time - integer, 2) < 0.01 else '0' + minute}'
    
    return hours

print(to_normal(98.05))
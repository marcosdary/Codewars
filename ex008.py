# tempo em segundo
# minuto = 60
# hora = 3600
# dia =   86400
# semana = 604800
from functools import reduce
tempo_segundos = 62

if tempo_segundos >= 604800:
    
    resultado_tempo = int(tempo_segundos/604800)
    if resultado_tempo == 1:
        print('uma semana atrás')
    else:
        print(f'{int(tempo_segundos/604800)} semanas atrás.')
        
elif 86400 <= tempo_segundos < 604800:
    
    resultado_tempo = int(tempo_segundos/ 86400)
    if resultado_tempo == 1:
        print('um dia atrás')
    else:
        print(f'{int(tempo_segundos/ 86400)} dias atrás.')  
        
elif 3600 <= tempo_segundos < 86400:
    
    resultado_tempo = int(tempo_segundos/3600)
    if resultado_tempo == 1:
        print('uma hora atrás')
    else:
        print(f'{int(tempo_segundos/3600)} horas atrás.')   
        
elif 60 <= tempo_segundos < 3600:
    
    resultado_tempo = int(tempo_segundos/60)
    if resultado_tempo == 1:
        print('um minuto atrás')
    else:
        print(f'{int(tempo_segundos/60)} minutos atrás.')
        
else:
    
    if tempo_segundos == 1:
        print('um segundo atrás')
    else:
        print(f'{int(tempo_segundos)} segundos atrás.')


# somente declarar o tempo em forma inteira

print(reduce(lambda ac, i: i/ac, tempo_segundos, 0))
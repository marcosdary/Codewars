# Escreva um programa que encontre a próxima sexta-feira 13 a partir da data atual


from datetime import datetime, timedelta

print(
    '''
            Encontre a próxima sexta-feira 13
                 Formato dd/mm/aaaa
    '''
)
data_1 = input("1° Data: ")

try:
    fmt = '%d/%m/%Y'
    data_atual = datetime.strptime(data_1, fmt)
    
    while True:
        
        if data_atual.weekday() == 4 and data_atual.day == 13:
            break
        data_atual += timedelta(days=1)
    data_sexta_feira = data_atual.strftime('%d-%m-%Y')
    print(f'Próxima sexta-feira 13 é na data: {data_sexta_feira}')
except ValueError:
    print(
        '''
                Uma das duas datas não possui o formato
                              proposto
        '''
    )


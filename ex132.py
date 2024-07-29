
from datetime import datetime, timedelta
print(
    '''
            Calculadora de Dias Úteis
              Formato dd/mm/aaaa
    '''
)
data_1 = input("1° Data: ")

data_2 = input("2° Data: ")

fmt = '%d/%m/%Y'
try:
    primeira_data = datetime.strptime(data_1, fmt)
    segunda_data = datetime.strptime(data_2, fmt)
    dia_atual = primeira_data
    dias_uteis = 0
    
    while dia_atual <= segunda_data:
        print(dia_atual.weekday())
        if dia_atual.weekday() < 5:
            dias_uteis += 1
        dia_atual += timedelta(days=1)

    print(
        f'''
                Quantidade de dias úteis: {dias_uteis}
        '''
    )    

except ValueError:
    print(
        """
                Uma das duas datas não possui o formato
                              proposto
        """
    )
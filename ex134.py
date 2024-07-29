# Escreva um programa que leia uma data no formato dd/mm/aaaa e 
# calcule quantos dias faltam até o final do ano
from datetime import datetime

print(
    '''
            Calculadora de quantos dias até final do ano
                        Formato dd/mm/aaaa HH:MM:SS
    '''
)
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')

print()
hora = input('Hora: ')
minuto = input('Minuto: ')
segundo = input('Segundo: ')
print()
data = f'{dia}/{mes}/{ano} {hora}:{minuto}:{segundo}'
fmt = '%d/%m/%Y %H:%M:%S'

ano_atual = datetime.now().date().year
data_final_ano = f'31/12/{ano_atual} 00:59:59'

try:
    data = datetime.strptime(data, fmt)
    data_final_ano = datetime.strptime(data_final_ano, fmt)

    if data.year != ano_atual:
        raise TypeError("A data deve ser desse ano")
    
    quantidade_dias_horas_minutos = data_final_ano - data
    horas = quantidade_dias_horas_minutos.seconds // 3600
    minutos = (quantidade_dias_horas_minutos.seconds % 3600) // 60
    segundos = (quantidade_dias_horas_minutos.seconds % 3600) % 60
    print(
        f'''
            
            São necessários {quantidade_dias_horas_minutos.days} dias {str(horas).zfill(2)}:{str(minutos).zfill(2)}:{str(segundos).zfill(2)}
                    para o fim do ano.
        '''
    )

except ValueError:
    print(
        """
                Uma das duas datas não possui o formato
                              proposto
        """
    )
except TypeError as err:
    print(
        f"""
                {err}
        """
    )

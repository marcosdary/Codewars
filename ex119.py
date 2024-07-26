# Escreva um programa que solicite ao usuário sua 
# data de nascimento no formato DD/MM/AAAA e calcule sua idade em anos

from datetime import datetime

print("""
                Calculadora de idade
      """
)
try:
    day = int(input('Dia: '))
    month = int(input('Mês: '))
    year = int(input('Ano: '))

    date = datetime(year, month, day)
    date_now = datetime.now()
    
    print(f'Idade: {(date_now.year - date.year) - 1 if date.month > date_now.month
                    else date_now.year - date.year} anos {abs(date_now.month - date.month)} meses {abs(date_now.day - date.day)} dias')
except ValueError:
    print(
        """
                Dados não estão no formato DD/MM/AAAA ou
                Valores não são inteiros
        """
    )
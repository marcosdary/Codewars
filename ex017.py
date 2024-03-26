def potencia_da_objeto(voltz, corrente): # operacao_realizada = '1'
    return voltz * corrente
    

def corrente_eletrica(quantidade_eletrons, tempo): # operacao_realizada = '2'
    try:
        delta_quantidade = quantidade_eletrons * 1.6
        return delta_quantidade/tempo
    
    except ZeroDivisionError: 
        return 'Não há divisão por 0'


def resistencia_do_resistor(resistividade, comprimento, area):  # operacao_realizada = '3'
    try:
        return resistividade*(comprimento/area)
    
    except ZeroDivisionError:
        return '\n\tNão há divisão por 0'
    
    
def voltagem(resistencia, corrente):  # operacao_realizada = '4'
    
    return resistencia*corrente
    
    
def calcular_voltagem():
    resistencia_user = float(input("Resistência: "))
    corrente_eletrica_user = float(input("Corrente: "))
    return f'Voltz: {voltagem(resistencia_user, corrente_eletrica_user)}V'

    
def calcular_resistencia():
    try:
        resistividade_user = float(input("Resistividade do objeto: "))
        comprimento_user = float(input("Comprimento: "))
        area_user = float(input("Área: "))
        return f'Resistor: {resistencia_do_resistor(resistividade_user, comprimento_user, area_user)}Ω'
    
    except ValueError:
        return "\n\tValores inválidos"


def calcular_corrente_eletrica():
    try:
        quantidade_eletrons_user = float(input("Quantidade de elétrons: "))
        tempo_user = float(input("Intervalo de tempo: "))
        return f'Corrente elétrica: {corrente_eletrica(quantidade_eletrons_user, tempo_user)}.10^-19A'
    except ValueError:
        return "\n\tValores inválidos"
  
    
def calcular_potencia():
    try:
        voltagem_user = float(input("Voltagem: "))
        corrente_eletrica_user = float(input("Corrente: "))
       
        return f'Potência: {potencia_da_objeto(voltagem_user, corrente_eletrica_user)}W'
    except ValueError:
        return "\n\tValores inválidos"


operacao_realizada = input('\t1. Potência elétrica\n\t2. Corrente elétrica\n\t3. Resistência elétrica\n\t4. Voltagem\nOperação: ')

operacao = {
    "1": lambda: calcular_potencia(), "2": lambda: calcular_corrente_eletrica(), 
    "3": lambda: calcular_resistencia(), "4": lambda: calcular_voltagem()
}
operacao_escolhida = operacao.get(operacao_realizada, None)
print("\n\tNão há essa opção") if operacao_escolhida is None else print(operacao_escolhida()) 
      

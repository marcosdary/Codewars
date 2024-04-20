# Divisibilidade 

# divisibilidade por 2
def divisibilidade(num):
    ultimo_dois_digitos= int(str(num)[-2:])
    ultimo_tres_digitos = int(str(num)[-3:])
    soma_digitos = sum([int(x) for x in str(num)])
    todos_os_digitos = int(str(num)[:-1])
    divisivel_sete = todos_os_digitos - ultimo_dois_digitos[0] * 2
    if num % 2 == 0:
        return 'Divisivel por 2'
    
    if ultimo_dois_digitos % 4 == 0:
        return 'Divisivel por 4'
    
    if soma_digitos % 3 == 0:
        return 'Divisivel por 3'
    
    if ultimo_dois_digitos[0] in [0, 5]:
        return 'Divisivel por 5'
    
    if num % 2 == 0 and soma_digitos % 3 == 0:
        return 'Divisivel por 6'
    
    if divisivel_sete % 7 == 0:
        return 'Divisivel por 7'
    
    if ultimo_tres_digitos % 8 == 0:
        return 'Divisivel por 8'
    
    if soma_digitos % 9 == 0:
        return 'Divisivel por 9'
    
    if ultimo_dois_digitos[0] == 0:
        return 'Divisivel por 10'
    
print('6'[-2])

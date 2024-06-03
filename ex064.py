DIGITO_VERIFICACAO = (2, 3, 4, 5, 6, 7)

def add_check_digit(numero):
    d = 0
    produtos = 0
    for i in reversed(numero):
        produtos += int(i)*DIGITO_VERIFICACAO[d]
    
        if d == len(DIGITO_VERIFICACAO)-1:
            d = -1
        d += 1
    
    soma_produtos = produtos % 11  
    novo_numero = numero 
    
    if soma_produtos == 0:
        novo_numero += '0'
        
    elif soma_produtos == 1:
        novo_numero += "X"
        
    else:
        
        novo_numero += str(11 - soma_produtos)
    
    return novo_numero

print(add_check_digit('167703625')) 
def isCpf(cpf:str):
    cpf = cpf.replace(".", '').replace('-', '')
    if cpf == 11:
        return False
    
    digito_verificador = 0
    for i in range(len(cpf[:9])):
        d = 10 - i
        if d > 1:
            digito_verificador += int(cpf[i]) * d
            
    digito_verificador = (digito_verificador * 10) % 11
    if digito_verificador == 10 or digito_verificador == 11:
        digito_verificador = 0
    
    if digito_verificador != int(cpf[9]):
        return False
    
    digito_verificador = 0
    for i in range(len(cpf[:10])):
        d = 11 - i
        if d > 1:
            digito_verificador += int(cpf[i]) * d
            
    digito_verificador = (digito_verificador * 10) % 11
    if digito_verificador == 10 or digito_verificador == 11:
        digito_verificador = 0
    if digito_verificador != int(cpf[10]):
        return False
    
    return True
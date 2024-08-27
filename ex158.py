# Válida um CPF

# Se o resto desta soma for menor ou igual a 1 e o penúltimo dígito do CPF deve ser igual ao numeral zero... 
# Entretanto se o resto for maior de 2, então o penúltimo dígito do CPF deve ser igual a diferença entre o numero 11 menos o valor do resto obtido
cpf_exemplo = '117.678.873'
cpf_exemplo_sem_pontos = list(cpf_exemplo.replace('.', '').replace('-',''))

def validar_cpf(cpf:list[str]):
    tamanho_penultimo = 10
    tamanho_ultimo = 11

    valores_operacao_penultimo = []
    valores_operacao_ultimo = []

    for digito in cpf:
        valores_operacao_penultimo.append(int(digito) * tamanho_penultimo)
        tamanho_penultimo -= 1
    soma_penultimo_digito = sum(valores_operacao_penultimo) % 11
    penultimo_digito = 11 - soma_penultimo_digito if soma_penultimo_digito > 2 else 0

    cpf.append(penultimo_digito)
    for digito in cpf:
        valores_operacao_ultimo.append(int(digito) * tamanho_ultimo)
        tamanho_ultimo -= 1

    
    soma_ultimo_digito = sum(valores_operacao_ultimo) % 11
    ultimo_digito = 11 - soma_ultimo_digito if soma_ultimo_digito > 2 else 0
    cpf.append(ultimo_digito)

    return ''.join(str(x) for x in cpf)
    
   
        

    
print(validar_cpf(cpf_exemplo_sem_pontos))

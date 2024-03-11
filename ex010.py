# Converter uma string hexadecimal em RGB
# #FF9933 == (255, 128, 0)
# FF or ff == 255
# Para converter um valor hexadecimal para RGB, você pode seguir este procedimento:

# Conversão de hexadecimal para inteiro: int(num_hex, 'hex')
# Para converter um valor hexadecimal para RGB, você pode seguir este procedimento:
# Separe os componentes de cor: Um valor hexadecimal de cor consiste em três pares de dígitos, representando os componentes vermelho, verde e azul, respectivamente.
# Converta os valores hexadecimais para decimais: Cada par de dígitos hexadecimais corresponde a um número decimal.Por exemplo, "FF" em hexadecimal é 255 em decimal.
# Atribua os valores decimais aos componentes de cor RGB: O primeiro par de dígitos hexadecimais corresponde ao componente de vermelho, o segundo ao componente de verde e o terceiro ao componente de azul.
# Por exemplo, se você tem o valor hexadecimal #FF0000, isso significa que o componente vermelho é FF (ou 255 em decimal), enquanto os componentes verde e azul são 00 (ou 0 em decimal). Portanto, a cor RGB correspondente seria (255, 0, 0).
# Aqui está um exemplo de como converter o valor hexadecimal #FFA500 (laranja) para RGB:
# Separamos os pares de dígitos: FF (vermelho), A5 (verde), 00 (azul).
# Convertemos cada par de dígitos hexadecimal para decimal: FF = 255, A5 = 165, 00 = 0.
# Atribuímos os valores decimais aos componentes de cor RGB: vermelho = 255, verde = 165, azul = 0.
# Portanto, a cor RGB correspondente ao valor hexadecimal #FFA500 é (255, 165, 0).'''
def hex_string_to_RGB(hex_string): 
    red, green, blue = hex_string[1:3], hex_string[3:5], hex_string[5:]
    
    rgb = {'r':conversion_hex(red), 'g':conversion_hex(green), 'b':conversion_hex(blue)}
    return rgb

def conversion_hex(num):
    return int(num, 16)



string = '#FFA500'
print(hex_string_to_RGB(string))


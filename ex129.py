# estamos usando paridade par: 
# o bit de paridade é definido como 0 
# se o número de 1 bits for par e como 1se for ímpar.
# parity_bit("10100011 00111001 11001100") -> "1010001 0011100 1100110"
# parity_bit("01101001 01101110 01100000 01010110 10001111 01100011") -> "0101100 error 0110000 0101011 error 0110001
from re import findall, compile

def parity_bit(binary):
    comp = compile(r'[01]+')
    
    binarys = findall(comp, binary)
    parity = [
        binary[:-1] if binary[:-1].count('1') % 2 == 0 and binary[-1] == '0'\
        or binary[:-1].count('1') % 2 != 0 and binary[-1] == '1' else \
        'error'
        for binary in binarys
    ]
    return ' '.join(parity)

print(parity_bit("01011001 01101110 01100000 01010110 10001111 01100011"))
    
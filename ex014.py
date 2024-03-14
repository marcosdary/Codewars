# +--------+-------+
# | Symbol | Value |
# +--------+-------+
# |    M   |  1000 |
# |   CM   |   900 |
# |    D   |   500 |
# |   CD   |   400 |
# |    C   |   100 |
# |   XC   |    90 |
# |    L   |    50 |
# |   XL   |    40 |
# |    X   |    10 |
# |   IX   |     9 |
# |    V   |     5 |
# |   IV   |     4 |
# |    I   |     1 |
# +--------+-------+


def to_roman(val : int) -> str:
        
        NUMBER_INT = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]                                     # Divida a seqüência de numeração romana em símbolos romanos (caractere).
        NUMBER_RAMON = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]                  # Converta cada símbolo de algarismos romanos no valor que ele representa.
                                                                                                                # Pegue o símbolo um por um a partir do índice 0: 
        i = 0                                                                                                   # Se o valor atual do símbolo for maior ou igual ao valor do próximo símbolo, adicione esse valor ao total corrente.
        number_ramon = ''                                                                                       # caso contrário, subtraia este valor adicionando o valor do próximo símbolo ao total corrente.    
        while i < len(NUMBER_INT):
                
                if val >= NUMBER_INT[i]:
                        div = val // NUMBER_INT[i]
                        val %= NUMBER_INT[i]
                        number_ramon += NUMBER_RAMON[i]*div           
                i += 1
        return number_ramon


def from_roman(roman_num : str) -> int:
        NUMBER_INT = [1000, 500, 100, 50, 10, 5, 1]                             # Inicialmente, o número = 3549, uma vez que 3549> = 1000; 
        NUMBER_RAMON = ["M", "D", "C", "L", "X", "V", "I"]                      #       o maior valor base será 1000 inicialmente. E Divide 3549/1000. Quociente = 3, 
        dict_int = {                                                            # Agora, o número se torna 549 e 1000> 549> = 500, o maior valor base será 500, 
                x:y                                                             #       então divida 549/500. Quociente = 1, Restante = 49. O símbolo correspondente D será repetido uma vez.
                for x, y in zip(NUMBER_RAMON, NUMBER_INT)                       # Agora, número = 49 e 50> 49> = 40, o maior valor base é 40. Em seguida, 
        }                                                                       #       divida 49/40. Quociente = 1, Restante = 9. O símbolo correspondente XL será repetido uma vez.
        number_int = 0                                                          # Agora, número = 9 e 10> 9> = 9, o maior valor base é 9. 
        i = 0                                                                   #       Em seguida, divida 9/9. Quociente = 1, Restante = 0. O símbolo correspondente IX será repetido uma vez.
        numbers = list(map(lambda r: dict_int[r], roman_num))                   # Finalmente, o número torna-se 0, o algoritmo pára aqui. A saída obtida MMMDXLIX.
        while i < len(numbers):
                v1 = numbers[i]
                if i + 1 < len(numbers):
                        v2 = numbers[i + 1]
                        if v1 >= v2:
                                number_int += v1
                                i += 1
                        else:
                                number_int += v2 - v1
                                i += 2
                else:           
                        number_int += v1
                        i =+ 1 
        return number_int


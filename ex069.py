LETTER = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
    'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 
    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
    's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

def high(x:str):

    lista_palavra = x.split()
    dicionario_palavra = {}
    for palavra in lista_palavra:
        s = 0
        for letra in palavra:
            s += LETTER.get(letra)
        dicionario_palavra[palavra] = s

    maior_letra = list(dicionario_palavra.keys())[0]
    s = list(dicionario_palavra.values())[0]

    for key in dicionario_palavra.keys():
        if dicionario_palavra[key] > s:
            s = dicionario_palavra[key]
            maior_letra = key
   
    return maior_letra


frase = 'take me to semynak'
print(high(frase))
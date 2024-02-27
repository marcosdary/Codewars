def decode(r):
    list_word = [
        'a', 'b', 'c', 'd', 'e', 'f',
        'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x',
        'y', 'z'
    ]
    num = ''
    string = ''
    new_string = ''
    for i in r:
        if i.isnumeric():
            num += i
        else:
            string += i
    exemple = "uogbucwnddunktsjfanzlurnyxmx"
    
        index_string = list_word.index(s)
        calculo = index_string * int(num) % 26
        
    
        
    return 0

output = decode("6015ekx")#decode("1273409kuqhkoynvvknsdwljantzkpnmfgf")
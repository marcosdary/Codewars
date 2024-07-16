def pis_pasep(pis: str) -> bool:
    end_digit = int(pis[-1])
    pis = pis.replace('.', '').replace('-', '')
    if len(pis) != 11:
        return False     
    sm = 0
    d = 2
    for i in reversed(range(len(pis)-1)):
        if d == 10:
            d = 2
        sm += int(pis[i]) * d
        d += 1

    rst = 11 - (sm % 11)
    ver_digit = rst if rst < 10 else 0
    return end_digit == ver_digit


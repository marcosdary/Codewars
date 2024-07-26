from re import findall, sub, I
def fake_bin(x):
    return ''.join(['0' if int(x[y]) < 5 else '1' for y in range(0, len(x))])
print(fake_bin("45385593107843568")) # -> "01011110001100111"
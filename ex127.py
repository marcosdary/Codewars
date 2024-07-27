def amount_of_pages(summary):
    i = 1
    digitos = ''
    while i <= summary:
        digitos += str(i)
        print(len(digitos))
        if len(digitos) == summary:
            return i
        i += 1
print(amount_of_pages(5))
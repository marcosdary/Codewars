def sort_reindeer(reindeer_names):
    reindeer_names = sorted(map(lambda a: a.split(' '), reindeer_names), key= lambda a: a[1])
    return [' '.join(a) for a in reindeer_names]

print(sort_reindeer(['Kenjiro Mori', 'Susumu Tokugawa', 'Juzo Okita', 'Akira Sanada'])) #=> ['Kenjiro Mori', 'Juzo Okita', 'Akira Sanada', 'Susumu Tokugawa']
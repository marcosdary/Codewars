# Matriz 20x20
# alturas
# média geral da população da amostra
# quantidade de pessoas que estão abaixo da média geral

altura_matriz = [
    [1.78, 1.92, 1.65, 1.82, 1.54, 1.99, 1.87, 1.60, 1.93, 1.75, 1.66, 1.58, 1.85, 1.77, 1.89, 1.61, 1.80, 1.64, 1.90, 1.73],
    [1.83, 1.55, 1.78, 1.92, 1.61, 1.88, 1.67, 1.84, 1.79, 1.91, 1.62, 1.71, 1.99, 1.68, 1.53, 1.85, 1.74, 1.63, 1.76, 1.95],
    [1.81, 1.73, 1.58, 1.67, 1.64, 1.89, 1.72, 1.55, 1.91, 1.77, 1.70, 1.93, 1.62, 1.54, 1.80, 1.85, 1.78, 1.66, 1.82, 1.59],
    [1.70, 1.79, 1.61, 1.92, 1.88, 1.75, 1.90, 1.83, 1.68, 1.95, 1.76, 1.67, 1.57, 1.82, 1.99, 1.87, 1.74, 1.66, 1.53, 1.65],
    [1.93, 1.71, 1.85, 1.60, 1.83, 1.54, 1.81, 1.64, 1.59, 1.90, 1.77, 1.78, 1.62, 1.84, 1.99, 1.75, 1.73, 1.69, 1.56, 1.91],
    [1.86, 1.74, 1.58, 1.77, 1.68, 1.94, 1.67, 1.92, 1.61, 1.53, 1.70, 1.83, 1.63, 1.89, 1.82, 1.55, 1.80, 1.91, 1.72, 1.65],
    [1.75, 1.88, 1.60, 1.77, 1.93, 1.67, 1.82, 1.64, 1.87, 1.91, 1.55, 1.68, 1.74, 1.90, 1.72, 1.65, 1.79, 1.58, 1.83, 1.54],
    [1.61, 1.95, 1.70, 1.82, 1.64, 1.90, 1.75, 1.59, 1.89, 1.78, 1.72, 1.66, 1.85, 1.60, 1.54, 1.87, 1.73, 1.93, 1.68, 1.57],
    [1.71, 1.83, 1.68, 1.88, 1.79, 1.55, 1.74, 1.66, 1.90, 1.61, 1.77, 1.63, 1.56, 1.93, 1.70, 1.91, 1.64, 1.58, 1.89, 1.75],
    [1.87, 1.59, 1.77, 1.64, 1.91, 1.72, 1.58, 1.89, 1.83, 1.66, 1.80, 1.95, 1.62, 1.54, 1.74, 1.78, 1.70, 1.85, 1.68, 1.93],
    [1.67, 1.79, 1.55, 1.89, 1.91, 1.61, 1.83, 1.69, 1.92, 1.77, 1.68, 1.84, 1.60, 1.54, 1.71, 1.85, 1.73, 1.88, 1.56, 1.94],
    [1.75, 1.90, 1.59, 1.68, 1.71, 1.62, 1.88, 1.56, 1.86, 1.78, 1.74, 1.63, 1.60, 1.95, 1.83, 1.91, 1.77, 1.70, 1.67, 1.85],
    [1.68, 1.92, 1.61, 1.78, 1.89, 1.72, 1.54, 1.82, 1.65, 1.90, 1.77, 1.83, 1.58, 1.75, 1.87, 1.56, 1.71, 1.88, 1.64, 1.95],
    [1.73, 1.79, 1.55, 1.81, 1.67, 1.84, 1.90, 1.68, 1.62, 1.85, 1.60, 1.75, 1.56, 1.88, 1.92, 1.74, 1.91, 1.78, 1.63, 1.86],
    [1.81, 1.66, 1.90, 1.75, 1.62, 1.84, 1.56, 1.69, 1.55, 1.77, 1.94, 1.88, 1.71, 1.91, 1.64, 1.78, 1.85, 1.68, 1.60, 1.87],
    [1.64, 1.88, 1.70, 1.73, 1.62, 1.80, 1.75, 1.90, 1.66, 1.58, 1.85, 1.71, 1.92, 1.67, 1.83, 1.94, 1.78, 1.60, 1.69, 1.55],
    [1.83, 1.54, 1.87, 1.65, 1.91, 1.79, 1.59, 1.74, 1.68, 1.85, 1.70, 1.92, 1.62, 1.55, 1.88, 1.77, 1.73, 1.80, 1.67, 1.66],
    [1.90, 1.64, 1.82, 1.77, 1.69, 1.86, 1.72, 1.61, 1.84, 1.78, 1.56, 1.91, 1.55, 1.87, 1.75, 1.60, 1.85, 1.67, 1.73, 1.68],
    [1.71, 1.63, 1.78, 1.65, 1.87, 1.62, 1.91, 1.79, 1.59, 1.88, 1.70, 1.85, 1.54, 1.60, 1.92, 1.75, 1.68, 1.84, 1.77, 1.64],
    [1.87, 1.55, 1.81, 1.74, 1.90, 1.79, 1.58, 1.83, 1.68, 1.65, 1.85, 1.63, 1.91, 1.56, 1.77, 1.70, 1.75, 1.84, 1.86, 1.54]
]

def dados_populacao_altura(alturas:list) -> dict:
   
    i = sum(len(alt) for alt in alturas)
    media_alturas = sum(n for alt in alturas for n in alt) / i
    quantidade_menor_media = sum(1 for alt in alturas for n in alt if n < media_alturas)
    return {'media': round(media_alturas, 2), 'qtd': quantidade_menor_media}

print(dados_populacao_altura(altura_matriz))
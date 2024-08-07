pesquisa = [
    (7213.53, 1), (4386.19, 2), (3642.11, 1), (9264.34, 3), (8117.66, 1),
    (7061.82, 2), (5861.39, 3), (5216.11, 2), (2145.94, 1), (8754.22, 2),
    (7942.50, 1), (6813.84, 3), (9336.12, 1), (8472.37, 2), (4692.43, 3),
    (2571.67, 1), (7144.19, 3), (8835.95, 2), (3452.75, 1), (7791.50, 3),
    (4291.94, 1), (5245.82, 2), (9764.83, 3), (7462.71, 1), (3961.58, 2),
    (5683.12, 3), (2725.79, 1), (6317.44, 2), (8521.17, 3), (7844.32, 1),
    (3127.98, 3), (6789.11, 1), (4951.30, 2), (9564.67, 3), (8472.88, 1),
    (7519.45, 2), (5869.33, 3), (4231.56, 1), (2791.34, 2), (8921.56, 3),
    (7352.48, 1), (4576.94, 3), (3681.22, 2), (8756.31, 1), (7924.37, 3),
    (6812.39, 2), (9354.72, 1), (8467.55, 2), (4931.71, 3), (2147.32, 1),
    (7153.22, 3), (8894.50, 2), (3421.58, 1), (7771.12, 3), (4192.35, 1),
    (5236.81, 2), (9721.34, 3), (7456.98, 1), (3917.56, 2), (5653.78, 3),
    (2711.47, 1), (6298.19, 2), (8507.34, 3), (7834.91, 1), (3109.85, 3),
    (6752.32, 1), (4934.21, 2), (9536.47, 3), (8441.78, 1), (7498.64, 2),
    (5832.15, 3), (4191.56, 1), (2763.79, 2), (8905.17, 3), (7317.48, 1),
    (4542.68, 3), (3665.39, 2), (8722.56, 1), (7901.43, 3), (6783.49, 2),
    (9321.16, 1), (8452.45, 2), (4894.79, 3), (2137.34, 1), (7135.49, 3),
    (8871.43, 2), (3405.17, 1), (7748.29, 3), (4165.78, 1), (5207.39, 2),
    (9703.45, 3), (7428.98, 1), (3895.29, 2), (5631.38, 3), (2694.38, 1),
    (6273.98, 2), (8489.47, 3), (7813.98, 1), (3093.75, 3), (6725.67, 1)
]

def dados_pesquisa(dados: list[tuple]) -> dict:
    qualidade = {'Boa': 0, 'Regular': 0, 'Ruim': 0}
    tamanho = len(dados)
    salario = 0

    for salario_dado, tipo_qualidade in dados:
        match tipo_qualidade:
            case 1:
                qualidade['Boa'] += 1
            case 2:
                qualidade['Regular'] += 1
            case 3:
                qualidade['Ruim'] += 1

        salario += salario_dado

    escolha_maior = max(qualidade.items(), key=lambda k: k[1]) if qualidade['Boa'] != qualidade['Regular'] != qualidade['Ruim'] else 0
    return {'qualidade_do_produto': escolha_maior[0], 'salario': round(salario / tamanho, 2)}

print(dados_pesquisa(pesquisa))
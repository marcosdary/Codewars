def cakes(recipe: dict, available: dict):
    list_recipe = sorted(recipe.items(), key=lambda value: value[1], reverse= True)
    key_recipe = list_recipe[0][0]
    soma_maior_ingrediente, numero_maximo_de_bolos = 0, 0
    while True:
        soma_maior_ingrediente += list_recipe[0][1]
        if soma_maior_ingrediente > available[key_recipe]:
            return numero_maximo_de_bolos
        
        numero_maximo_de_bolos += 1

dict_ingredientes_receita =  {"sugar": 500, "flour": 2000, "milk": 2000}
dict_requisitos_receita =  {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}

output = cakes(dict_requisitos_receita, dict_ingredientes_receita)
print(output)

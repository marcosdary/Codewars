def cakes(recipe:dict, available:dict):
    try:
        ingredientes = {k:available[k] for k in recipe}
        menor_quantidade = [ingredientes[k]//recipe[k] for k in ingredientes.keys()] 
        return min(menor_quantidade)
    except KeyError:
        return 0

print(cakes({'cream': 38, 'nuts': 75, 'pears': 17}, {'flour': 3415, 'cream': 9037, 'apples': 375, 'cocoa': 8232, 'pears': 429, 'oil': 7990, 'nuts': 1641, 'eggs': 6865, 'crumbles': 5813, 'chocolate': 8345}))
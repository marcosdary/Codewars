import collections
def sorted_brands(history):
    marcas = list(
        map(lambda produto: produto['brand'], history)
    )
    marcas_populares = collections.Counter(marcas)
    
    marcas_populares = sorted(marcas_populares.items(), key= lambda x: x[1], reverse=True)

    return list(x for x, _ in marcas_populares)
history = [{'name': 'LG Phone1', 'price': 35, 'brand': 'LG'}, {'name': 'Google Nexus3', 'price': 50, 'brand': 'Google Nexus'}, 
           {'name': 'Samsung Phone1', 'price': 25, 'brand': 'Samsung'}, {'name': 'Google Nexus2', 'price': 35, 'brand': 'Google Nexus'}, 
           {'name': 'Samsung Phone2', 'price': 5, 'brand': 'Samsung'}, {'name': 'Samsung Phone1', 'price': 25, 'brand': 'Samsung'},
           {'name': 'Samsung Phone1', 'price': 25, 'brand': 'Samsung'}, {'name': 'LG Phone1', 'price': 35, 'brand': 'LG'}, 
           {'name': 'Google Nexus3', 'price': 50, 'brand': 'Google Nexus'}, {'name': 'Google Nexus3', 'price': 50, 'brand': 'Google Nexus'}, 
           {'name': 'Samsung Phone1', 'price': 25, 'brand': 'Samsung'}, {'name': 'Google Nexus2', 'price': 35, 'brand': 'Google Nexus'}, 
           {'name': 'Samsung Phone1', 'price': 25, 'brand': 'Samsung'}, {'name': 'LG Phone1', 'price': 35, 'brand': 'LG'}, 
           {'name': 'Samsung Phone3', 'price': 15, 'brand': 'Samsung'}, {'name': 'Nokia Phone2', 'price': 1, 'brand': 'Nokia'}, 
           {'name': 'Samsung Phone2', 'price': 5, 'brand': 'Samsung'}, {'name': 'Samsung Phone1', 'price': 25, 'brand': 'Samsung'}, 
           {'name': 'Nokia Phone2', 'price': 1, 'brand': 'Nokia'}, {'name': 'LG Phone1', 'price': 35, 'brand': 'LG'}, 
           {'name': 'Google Nexus1', 'price': 25, 'brand': 'Google Nexus'}, {'name': 'LG Phone2', 'price': 25, 'brand': 'LG'}, 
           {'name': 'Google Nexus1', 'price': 25, 'brand': 'Google Nexus'}, {'name': 'LG Phone1', 'price': 35, 'brand': 'LG'}, 
           {'name': 'Google Nexus1', 'price': 25, 'brand': 'Google Nexus'}, {'name': 'Samsung Phone3', 'price': 15, 'brand': 'Samsung'}, 
           {'name': 'Nokia Phone2', 'price': 1, 'brand': 'Nokia'}, {'name': 'Google Nexus1', 'price': 25, 'brand': 'Google Nexus'}, 
           {'name': 'LG Phone1', 'price': 35, 'brand': 'LG'}, {'name': 'Samsung Phone3', 'price': 15, 'brand': 'Samsung'}, 
           {'name': 'Samsung Phone1', 'price': 25, 'brand': 'Samsung'}, {'name': 'Samsung Phone2', 'price': 5, 'brand': 'Samsung'}
]
print(sorted_brands(history)) # ['Samsung', 'Google Nexus', 'LG', 'Nokia']
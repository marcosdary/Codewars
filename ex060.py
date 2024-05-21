class Dicionario:
    
    def __init__(self, dicionario_1:dict, dicionario_2:dict) -> None:
        self._dicionaro_1 = dicionario_1
        self._dicionaro_2 = dicionario_2
        
    def modificar_valor(self, chave, novo_valor, opcao:int):
        
        if opcao == 1:
            
            if chave in self._dicionaro_1.keys():
                self._dicionaro_1[chave] = novo_valor
                return 'Valor modificado com sucesso!!'
            else:
                return f'Não há {chave} no dicionário'
            
        elif opcao == 2:
            
            if chave in self._dicionaro_2.keys():
                self._dicionaro_2[chave] = novo_valor
                return 'Valor modificado com sucesso!!'
            else:
                return f'Não há {chave} no dicionário'
        
        raise ValueError("opção não encontrado")
    
    def verificar_chave(self, chave, opcao:int):
        
        if opcao == 1:
            
            if chave in self._dicionaro_1.keys():
    
                return 'Chave encontrada com sucesso!!'
            else:
                return f'Não há {chave} no dicionário'
            
        elif opcao == 2:
            
            if chave in self._dicionaro_2.keys():

                return 'Chave encontrada com sucesso!!'
            else:
                return f'Não há {chave} no dicionário'
        
        raise ValueError("opção não encontrado")
            
    def remover_chave(self, chave, opcao:int):
        
        if opcao == 1:
            
            if chave in self._dicionaro_1.keys():
                del self._dicionaro_1[chave]
                return 'Chave removida com sucesso!!'
            else:
                return f'Não há {chave} no dicionário'
            
        elif opcao == 2:
            
            if chave in self._dicionaro_2.keys():
                del self._dicionaro_2[chave]
                return 'Chave removida com sucesso!!'
            else:
                return f'Não há {chave} no dicionário'
        
        raise ValueError("opção não encontrado")
            
    def listar_dicionario(self, opcao:int):
        
        if opcao == 1:
            return list(self._dicionaro_1.items())
            
        elif opcao == 2:
            
            return list(self._dicionaro_2.items())
        
    def iterar(self, opcao:int):
        
        if opcao == 1:
            texto = ''
            texto += f'{"Nome": <10} {"Idade(anos)"}\n'
            for chave, valor in self._dicionaro_1.items():
                texto += f'{chave: <10} {valor}\n'
                
            return texto
            
        elif opcao == 2:
            texto = ''
            texto += f'{"Cidade": <19} {"População"}\n'
            for chave, valor in self._dicionaro_2.items():
                texto += f'{chave: <20}{valor}\n'
                
            return texto
        
        raise ValueError("opção não encontrado")
          
# Dicionário com nomes e idades
nomes_idades = {
    'Ana': 30,
    'Carlos': 25,
    'Beatriz': 27,
    'Eduardo': 35,
    'Fernanda': 28,
    'Guilherme': 31,
    'Helena': 29,
    'Igor': 32,
    'Juliana': 26,
    'Kleber': 33
}

# Dicionário com cidades e populações
cidades_populacoes = {
    'São Luís': 1101884,
    'Teresina': 868075,
    'Fortaleza': 2669342,
    'Natal': 890480,
    'João Pessoa': 809015,
    'Recife': 1653461,
    'Maceió': 1029129,
    'Aracaju': 664908,
    'Salvador': 2886698,
    'Manaus': 2219580
}

dicionario_nome_pop = Dicionario(nomes_idades, cidades_populacoes)
print(dicionario_nome_pop.verificar_chave('Manaus', 2))
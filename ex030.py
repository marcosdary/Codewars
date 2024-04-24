class Produto: 
    def __init__(self) -> None:
        self._nome = None
        self._preco = 0
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome:str):
        if all(x.isalnum() or x.isspace() for x in nome):
            self._nome = nome
        else:
            print(" "*15, "Este nome está inválido")
         
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco):
        try:
            if float(preco) > 0:
                self._preco = float(preco) 
            else:
                raise ValueError  
        except ValueError:
            print(" "*15, "Preço inválido")
    
    def desconto(self, dst):
        
        valor_descontado = self._preco * dst
        return valor_descontado
        


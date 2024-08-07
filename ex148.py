class ProdutoCartesiano:
    def __init__(self, a:list[int], b:list[int]) -> None:
        self.a = a
        self.b = b

    def produtoaxb(self):
        axb = []
        for na in self.a:
            for nb in self.b:
                axb.append((na, nb))
        return axb
    
    def qtd_elemento(self):
        return len(self.a) * len(self.b)
    
a = [1,2,3] 
b = [1,2,3]

produto_cartesiano = ProdutoCartesiano(a, b)
print(produto_cartesiano.produtoaxb())
print(produto_cartesiano.qtd_elemento())
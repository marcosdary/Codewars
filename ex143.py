class OperacaoAritmetica:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def subtracao(self) -> float:
        return self.a - self.b
    
    def potenciacao(self) -> float:
        return pow(self.a, self.b)
    
    def divisao(self) -> float:
        return self.a / self.b 
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}(a={self.a},b={self.b})'
    

def operacao(a:float, b:float, op:int) -> str|float:
    if a > 0 and b > 0:
        operacao_aritmetica = OperacaoAritmetica(a, b)
        match op:
            case 1:
                return operacao_aritmetica.subtracao()
            case 2:
                return operacao_aritmetica.potenciacao()
            case 3:
                return operacao_aritmetica.divisao()
            case _:
                return 'Escolha uma das opções'
            
    return 'Números maiores que zero'


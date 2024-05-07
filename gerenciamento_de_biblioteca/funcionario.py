from pessoa import Pessoa

class Funcionario(Pessoa):
    
    def __init__(self, nome, idade, cargo) -> None:
        
        super().__init__(nome, idade)
        self._cargo = cargo
        self.__senha_acesso = None

    @property
    def cargo(self):
        
        return self._cargo
    
    @cargo.setter
    def cargo(self, cargo):
        
        self._cargo = cargo
    
    def senha_acesso(self, senha):
        
        self.__senha_acesso = senha
            
    def acesso_servidor(self, senha):
        
        if senha == self.__senha_acesso:
            return 'Acesso válido'
        
        raise ValueError('Acesso negado')
            
    def __str__(self) -> str:
        return f'\tOlá {self.nome}, como cê tá?\n\tMeu cargo é: {self._cargo}'
# Crie quatro classes: Funcionario, Cliente, FuncionarioCliente e ClienteFuncionario. Funcionario e Cliente devem ter um método mostrar_identidade() 
# que imprime "Identidade Funcionário" e "Identidade Cliente", respectivamente.
# FuncionarioCliente deve herdar de Funcionario e Cliente, enquanto ClienteFuncionario deve herdar de Cliente e Funcionario. Ambas as classes 
# FuncionarioCliente e ClienteFuncionario devem implementar um método mostrar_relacao(), que imprime "Relação Funcionário e Cliente" e "Relação Cliente e Funcionário", respectivamente.

class Funcionario:
    
    def mostrar_identidade(self):
        print("Identidade Funcionário")
        
class Cliente:
    
    def mostrar_identidade(self):
        print("Identidade Cliente")
        
class FuncionarioCliente(Funcionario, Cliente):
    
    def mostrar_relacao(self):
        print('Relação Funciionário e Cliente')
        
class ClienteFuncionario(Funcionario, Cliente):
    
    def mostrar_relacao(self):
        print('Relação Cliente e Funciionário')
        
# Saída das Classes
print(f"Classe: {ClienteFuncionario.__name__}")
ClienteFuncionario().mostrar_identidade()
ClienteFuncionario().mostrar_relacao()
print('\n')
print(f"Classe: {FuncionarioCliente.__name__}")
FuncionarioCliente().mostrar_identidade()
FuncionarioCliente().mostrar_relacao()
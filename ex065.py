class InvalidValueError(Exception):
    pass

class InsufficientfundsError(Exception):
    pass

def throw(exception_, msg):
    exc = exception_(msg)
    raise exc

class BankAccount:
    
    def __init__(self, name:str) -> None:
        self._nome = name
        self._balance = 0
        
    def deposit(self, value:float):
        if value > 0:
            self._balance += value
            return 'Depósito realizado com sucesso'
        
        throw(InvalidValueError, 'Valor inválido para depósito')
        
    def widthdraw(self, value:float):
        if value > 0 :
            if value <= self._balance:
                self._balance -= value
                return 'Saque realizado com sucesso'
            else:
                throw(InsufficientfundsError, 'Saque não pode ser realizado')
        throw(InvalidValueError, 'Valor inválido para o saque')
    
    @property
    def balance(self):
        return f'Saldo atual: {self._balance}'
    
class DataInput:
    
    @staticmethod
    def decimal_value(valor:str):
        if valor.isdecimal():
            return True
        return False
   
name = str(input("Nome: ")) 
bank = BankAccount(name)
while True:
    try:
        if name.isalpha():
            print("\t1. Depósito\n\t2. Saque\n\t3. Consulta\n\t4. Sair")
            option = input("Escolha: ")

            if option in ['1', '2', '3', '4']:
                
                if option == '1':
                    deposit_value = input("\nDepósito: ")
                    deposit_made = bank.deposit(float(deposit_value)) if DataInput().decimal_value(deposit_value) else throw(InvalidValueError, 'valor para depósito está inválido')
                    print('\n', deposit_made, '\n')
            
                elif option == '2':
                    withdrawal_value = input("\nSaque: ")
                    withdrawal_made = bank.widthdraw(float(withdrawal_value)) if DataInput().decimal_value(withdrawal_value) else throw(InvalidValueError, 'valor para saque está inválido')
                    print('\n', withdrawal_made, '\n')
                elif option == '3':
                    print(f'\n\t{bank.balance}\n')
                else:
                    print("\n\nObrigado pela escolha\n")
                    break
            
            else:
                throw(InvalidValueError, 'Escolha uma das opções')
        else:
            throw(InvalidValueError, 'Devem ser palavras')
            
    except (InsufficientfundsError, InvalidValueError) as err:
        print(f'\n{err.__class__.__name__}: {err}\n')
        
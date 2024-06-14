class NotNumberZeroError(Exception):
    def __init__(self) -> None:
        message = 'Não pode haver o número zero'
        super().__init__(message)

class FormatNotNumberError(Exception):
    def __init__(self) -> None:
        message = 'O formato do número é inválido'
        super().__init__(message)        

def iszero(num:int):
    if num == 0:
        exception_ = NotNumberZeroError()
        exception_.add_note("Ei programdor, arruma isso ai no tratamento de exceções")
        exception_.add_note("Falow programador .....")
        raise exception_   
    return num

def isnumber(num:str):
    if not num.isdigit():
        exception_ = FormatNotNumberError()
        exception_.add_note("Ei programdor, arruma isso ai no tratamento de exceções")
        exception_.add_note("Falow programador .....")
        raise exception_   
    return num

try: 
    num = 'Sou número'
    print(f"Seu número {isnumber(num)} não é zero")
    
except (NotNumberZeroError, FormatNotNumberError) as err:
    print(f"Error: {err}")       
    print('Notas')
    for nota in err.__notes__:
        print(nota) 
        


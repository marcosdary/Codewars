def decorator_user(func):
    def inner_user(*args, **kwargs):
        password = input("Senha do usuário: ")
        if password == "bit@**/":
            return func(*args, **kwargs)
        return '\tAcesso Negado'
    return inner_user

@decorator_user
def subtracao(a, b):
    return a - b
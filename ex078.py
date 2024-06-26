def decodificador(metodo): # Função decodificador recebe o retorno da função e decodificar a mensagem
    def interno(self, *args, **kwargs):
        r = metodo(self, *args, **kwargs)
        return f'Mensagem decoficada: "{r}"' 
    return interno


class Mensagem: # A classe Mensagem recebe o atributo com um texto codificado
    def __init__(self, texto) -> None:
        self.texto = texto

    @decodificador 
    def descodificar(self): # Esse método deve usar a função para decodifcar o texto e retorna a mensagem decodificada
        return self.texto
    
# Crie um decorador validar_argumentos que recebe uma lista de tipos de dados como parâmetros.
# Decore um método em uma classe com o decorador validar_argumentos.
# O decorador validar_argumentos deve verificar se os argumentos passados para o método são do tipo correto.
# Se um argumento for inválido, levante uma exceção TypeError.

def validar_argumento(metodo):
    def interno(self, *args, **kwargs):
        validador = is_integer(*args, *kwargs)
        if validador:
            return metodo(self, *args, **kwargs)
        raise TypeError("Argumentos passados não correspondem aos requisitados pelo método")
    return interno

def is_integer(integer):
    if isinstance(integer, int):
        return True
    return False

class OperacaoMatematica:
    def __init__(self, numero) -> None:
        self.numero = numero

    @validar_argumento
    def potencia(self, numero):
        return numero ** self.numero
    
numero = OperacaoMatematica(7)
print(numero.potencia(7))

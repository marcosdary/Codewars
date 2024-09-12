class Evento:
    def __init__(self, nome:str, data:str, local:str, capacidade_maxima:int) -> None:
        self.nome = nome
        self.data = data
        self.local = local
        self.lista_participante = []
        self.capacidade_maxima = capacidade_maxima

class Pessoa: 
    def __init__(self, id_pessoa:int, nome:str) -> None:
        self.id_pessoa = id_pessoa
        self.nome = nome

class Participante(Pessoa):
    def __init__(self, id_pessoa: int, nome: str) -> None:
        super().__init__(id_pessoa, nome)

    def inscrever(self, evento:Evento):
        total = len(evento.lista_participante) + 1
        if total <= evento.capacidade_maxima:
            evento.lista_participante.append(self.__dict__)
            return True
        return False
    
    def desinscrever(self, evento:Evento):
        if self.__dict__ in evento.lista_participante:
            evento.lista_participante.remove(self.__dict__)
            return True
        return False

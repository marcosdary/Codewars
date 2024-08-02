from datetime import datetime
from dateutil.relativedelta import relativedelta

class CalculadoraIdade:
    def __new__(cls, *args, **kwds):
        if not (kwds['dia'] <= 31 and kwds['mes'] <= 12 and kwds['ano'] <= datetime.now().year):
            raise ValueError("Data incompátivel com formato AAAA/MM/DD")
        return super().__new__(cls)
    def __init__(self, dia, mes, ano) -> None:
        self.dia = dia 
        self.mes = mes
        self.ano = ano
        self.__data = datetime.strptime(f'{self.ano}-{self.mes}-{self.dia}', '%Y-%m-%d')

    def idade(self):
        ida = relativedelta(datetime.now().date(), self.__data).years
        return ida

    def __repr__(self) -> str:
        return f'{type(self).__name__}(dia={self.dia},mes={self.mes},ano={self.ano})'


def maioridade(dia:int, mes:int, ano:int) -> bool:
    return True if CalculadoraIdade(dia=dia, mes=mes, ano=ano).idade() >= 18 else False
try:
    print(maioridade(12, 37, 2023))
except ValueError as err:
    print(f'ERROR: {err}')
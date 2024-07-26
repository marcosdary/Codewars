from datetime import datetime
class DataEHora:
    def __new__(cls, **kwds):
        instancia = super().__new__(cls)
        formato_data_hora = '%d/%m/%Y %H:%M'
       
        try:
            datetime.strptime(kwds['arg1'], formato_data_hora)
            datetime.strptime(kwds['arg1'], formato_data_hora)
            return instancia
        except ValueError:
            raise ValueError('Valor da Data e Hora na estão no formato espeficado')
        
    def __init__(self, arg1, arg2) -> None:
        self.arg1 = datetime.strptime(arg1, '%d/%m/%Y %H:%M')
        self.arg2 = datetime.strptime(arg2, '%d/%m/%Y %H:%M')

    def anterior_posterior(self):
        return f'Posterior: {self.arg1} Anterior: {self.arg2}' if datetime.timestamp(self.arg1) > datetime.timestamp(self.arg2) \
                else f'Posterior: {self.arg2} Anterior: {self.arg1}' if datetime.timestamp(self.arg1) > datetime.timestamp(self.arg2) \
                else 'Data e hora são iguais'
    

print(
    '''
                Data e hora anterior e posterior
                Formato permitido: DD/MM/AA HH:MM
    '''
)

data_1 = input('1° data e hora: ')

data_2 = input('2° data e hora: ')


dataehora = DataEHora(arg1=data_1, arg2=data_2)
print(
    f'''
        {dataehora.anterior_posterior()}
    '''
    )
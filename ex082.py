def salarioliquido(self):
    inss = self.aliquota_inss * self.salario
    irpf = self.aliquota_irpf * self.salario
    salario = self.salario - inss - irpf
    return salario 

class Meta(type):
    def __new__(mcs, name, bases, dct):
        cls = super().__new__(mcs, name, bases, dct)
        if cls.__name__ == 'SalarioLiquido':
            cls.salariototal = salarioliquido
        if 'aliquota_inss' not in cls.__dict__ or 'aliquota_irpf' not in cls.__dict__:
            raise NotImplementedError("Implemente o atributo da classe: aliquota_inss ou aliquota_irpf")
        return cls
    
    def __call__(self, *args, **kwds) :
        instance_ = super().__call__(*args, **kwds)
        if 'nome' not in instance_.__dict__:
            raise NotImplementedError('Implemente o atributo da instância: nome')
        return instance_
    
class SalarioLiquido(metaclass=Meta):
    aliquota_inss = 0.08
    aliquota_irpf = 0.075   

    def __new__(cls, *args, **kwds):

        x = super().__new__(cls)
        if kwds['salario'] < 0:
            raise ValueError('Atributo da instância inválido')
        return x 
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def __str__(self):
        return f'{self.nome} seu salário bruto é igual a {self.salario}'

    def __repr__(self):
        class_ = self.__class__.__name__
        return f'{class_}(nome={self.nome},salario={self.salario})'

class MetaPessoa(type):
    def __new__(mcs, name, bases, dct):
        cls = super().__new__(mcs, name, bases, dct)
        dict_class = cls.__dict__
        if '__repr__' not in dict_class and '__str__' not in dict_class:
            raise NotImplementedError('Implemente o métodos especias repr e str')
        if 'idade' not in dict_class:
            error = NotImplementedError('Implemente um property de idade')
            error.add_note('Utilize o property que atue como argumentos do objeto')
            raise error
        return cls
    
    def __call__(self, *args, **kwds):
        instancia = super().__call__(*args, **kwds)
        return instancia



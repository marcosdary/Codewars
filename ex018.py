class MassaCorporal:
    def __init__(self, nome_completo, peso, altura, sexo, idade):
        self.nome_completo = nome_completo
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.idade = idade
        self.imc = None
    
    def indice_massa_corporal(self):
        self.imc = round(float(self.peso)/pow(float(self.altura), 2), 3)
    
    def __str__(self):
        return f"""Detalhes: 
    \n\tNome completo - {self.nome_completo}\n\tIdade: {self.idade}\n\tSexo: {self.sexo}\n\tPeso: {self.peso}\n\tÍndice de massa corporal(IMC): {self.imc}
    """
  

pessoa_1 = MassaCorporal(nome_completo= 'marcos', peso=89, altura=1.78, sexo='masculino',idade= 20)
pessoa_1.indice_massa_corporal()

print(pessoa_1)
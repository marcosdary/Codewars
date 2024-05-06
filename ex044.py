class JurosCompostos:
    
    def __init__(self, capital:float, juros:float, tempo:int) -> None:
        self.capital = capital
        self.juros = juros/100
        self.tempo =tempo
        self._montante = None
        
    def calcular_motante(self):
        self._montante = self.capital * (1 + self.juros) ** self.tempo
        
    @property
    def montante(self):
        return self._montante
    
    
while True:
    try:
        capital = float(input("Valor do capital: "))

        juros = float(input("\nJuros: "))
        
        tempo = int(input("\nTempo: "))
    
        
        if capital > 0 and juros > 0 and tempo > 0:
            juros_compostos = JurosCompostos(capital, juros, tempo)
            juros_compostos.calcular_motante()
            print(f"\n\tO montante final após {tempo} meses será de R${juros_compostos.montante:.2f}")  
            break          
        else:
            raise ValueError('Values must be greater than 0')
    except ValueError as e:
        print(f"\n\tExceção: {e}\n")
    

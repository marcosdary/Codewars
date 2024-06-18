class Celsius:

    def __init__(self, x, op) -> None:
        self.x = x
        self.op = op
        
    def CelsiusKelvin(self):
        kel = (self.x + 273.15)
        return kel
    
    def CelsiusFahrenheit(self):
        fa = ((self.x * 9/5) + 32) 
        return fa
    
    def CelsiusRankine(self):
        ra = (self.x + 273.15) * (9/5)
        return ra
    
    def CelsiusRomer(self):
        ro = (self.x * (21/40)) + 7.5
        return ro
    
    def CelsiusNewton(self):
        n = self.x * (33/100)
        return n
    
    def CelsiusNewton(self):
        n = self.x * (33/100)
        return n
    
    def CelsiusReaumur(self):
        re = self.x * 0.8
        return re
    
    def CelsiusDelisle(self):
        de = (100 - self.x) * 1.5
        return de

    @property
    def operacao(self):
        calculo = {
            'K': self.CelsiusKelvin(), 'F': self.CelsiusFahrenheit(), 'R': self.CelsiusRankine(),
            'Ro': self.CelsiusRomer(), 'N': self.CelsiusNewton(), 'Re': self.CelsiusReaumur(),
            'De': self.CelsiusDelisle()
        }
        return int(calculo.get(self.op))

class Kelvin:

    def __init__(self, x, op) -> None:
        self.x = x
        self.op = op
        
    def KelvinCelsius(self):
        cel = (self.x - 273.15)
        return cel
    
    def KelvinFahrenheit(self):
        fa = ((self.x * 9/5) - 459.67) 
        return fa
    
    def KelvinRankine(self):
        ra = (self.x * (9/5))
        return ra 
    
    def KelvinNewton(self):
        n = (self.x - 273.15) * (33/100)
        return n
    
    def KelvinReaumur(self):
        re = (self.x - 273.15) * 0.8
        return re
    
    def KelvinRomer(self):
        ro = ((self.x - 273.15) * (21/40)) + 7.5
        return ro

    @property
    def operacao(self):
        calculo = {
            'C': self.KelvinCelsius(), 'F': self.KelvinFahrenheit(), 'R': self.KelvinRankine(),
            'N': self.KelvinNewton(), 'Re': self.KelvinReaumur(), 'Ro': self.KelvinRomer()
        }
        return int(calculo.get(self.op))
     
class Fahrenheit:

    def __init__(self, x, op) -> None:
        self.x = x
        self.op = op

    def FahrenheitCelsius(self):
        cel = (self.x - 32) * (5/9)
        return cel
    
    def FahrenheitKelvin(self):
        fa = (self.x + 459.67) / 1.8
        return fa
    
    def FahrenheitRankine(self):
        ra = (self.x + 459.67)
        return ra 
    
    def FahrenheitDelisle(self):
        de = (212 - self.x) * (5/6)
        return de
    
    def FahrenheitNewton(self):
        n = (self.x - 32) * (11/60)
        return n
    
    def FahrenheitReaumur(self):
        re =  (self.x - 32) / 2.25
        return re
    
    def FahrenheitRomer(self):
        ro =  ((self.x - 32) * (7/24)) + 7.5
        return ro
    
    @property
    def operacao(self):
        calculo = {
            'C': self.FahrenheitCelsius(), 'K': self.FahrenheitKelvin(), 'R': self.FahrenheitRankine(),
            'N': self.FahrenheitNewton(), 'Re': self.FahrenheitReaumur(), 'Ro': self.FahrenheitRomer(),
            'De': self.FahrenheitDelisle()
        }
        return int(calculo.get(self.op))
    
class Rankine:

    def __init__(self, x, op) -> None:
        self.x = x
        self.op = op

    def RankineCelsius(self):
        cel = (self.x - 491.67) * (5/9)
        return cel
    
    def RankineKelvin(self):
        kel = (self.x * (5/9)) 
        return kel
    
    def RankineFahrenheit(self):
        fa = (self.x - 459.67)
        return fa 

    def RankineReaumur(self):
        re = (self.x - 491.67) * (4/9)
        return re

    def RankineRomer(self):
        ro = ((self.x - 491.67) * (7/24)) + 7.5
        return ro

    def RankineNewton(self):
        n = (self.x - 491.67) * (11/60)
        return n

    def RankineDelisle(self):
        de = (671.67 - self.x) * (5/6)
        return de

    @property
    def operacao(self):
        calculo = {
            'C': self.RankineCelsius(), 'K': self.RankineKelvin(), 'F': self.RankineFahrenheit(),
            'Ro': self.RankineRomer(), 'N': self.RankineNewton(), 'Re': self.RankineReaumur(),
            'De': self.RankineDelisle()
        }
        return int(calculo.get(self.op))
    
class Delisle:

    def __init__(self, x, op) -> None:
        self.x = x
        self.op = op
        
    def DelisleCelsius(self):
        cel = 100 - (self.x * (2/3))
        return cel
    
    def DelisleKelvin(self):
        kel = 373.15 - (self.x * (2/3))
        return kel
    
    def DelisleFahrenheit(self):
        fa = 212 - (self.x * (6/5))
        return fa 
    
    def DelisleRankine(self):
        ra = 671.67 - (self.x * 1.2)
        return ra 
    
    def DelisleNewton(self):
        n = 33 - (self.x * 0.22)
        return n 

    def DelisleReaumur(self):
        re =  80 - (self.x * (8/15))
        return re 
    
    def DelisleRomer(self):
        ro = 60 - (self.x * 0.35)
        return ro 
    
    @property
    def operacao(self):
        calculo = {
            'C': self.DelisleCelsius(), 'K': self.DelisleKelvin(), 'F': self.DelisleFahrenheit(),
            'R': self.DelisleRankine(), 'N': self.DelisleNewton(), 'Re': self.DelisleReaumur(), 
            'Ro': self.DelisleRomer()    
        }
        return int(calculo.get(self.op))
    
class Newton:

    def __init__(self, x, op) -> None:
        self.x = x
        self.op = op
        
    def NewtonCelsius(self):
        cel = self.x * (100/33)
        return cel
    
    def NewtonKelvin(self):
        kel = (self.x * (100/33)) + 273.15
        return kel
    
    def NewtonFahrenheit(self):
        fa = (self.x * (60/11)) + 32
        return fa 
    
    def NewtonRankine(self):
        ra = (self.x * (60/11)) + 491.67
        return ra  
 
    def NewtonDelisle(self):
        de =  (33 - self.x) * (50/11)
        return de 
    
    def NewtonReaumur(self):
        re = self.x * (80/33)
        return re
    
    def NewtonRomer(self):
        ro = (self.x * (35/22)) + 7.5
        return ro
    
    @property
    def operacao(self):
        calculo = {
            'C': self.NewtonCelsius(), 'K': self.NewtonKelvin(), 'F': self.NewtonFahrenheit(),
            'R': self.NewtonRankine(),  'De': self.NewtonDelisle(), 'Re': self.NewtonReaumur(),
            'Ro': self.NewtonRomer()
        }
        return int(calculo.get(self.op))
    
class Reaumur:

    def __init__(self, x, op) -> None:
        self.x = x
        self.op = op
        
    def ReaumurCelsius(self):
        cel = self.x * (5/4)
        return cel
    
    def ReaumurKelvin(self):
        kel = (self.x * (5/4)) + 273.15
        return kel
    
    def ReaumurFahrenheit(self):
        fa = (self.x * (9/4)) + 32
        return fa 
    
    def ReaumurRankine(self):
        ra = (self.x * (9/4)) + 491.67
        return ra
    
    def ReaumurNewton(self):
        n = self.x * (33/80)
        return n
    
    def ReaumurRomer(self):
        ro = (self.x * (21/32)) + 7.5
        return ro
    
    def ReaumurDelisle(self):
        de = (80 - self.x) * 1.875
        return de
    
    @property
    def operacao(self):
        calculo = {
            'C': self.ReaumurCelsius(), 'K': self.ReaumurKelvin(), 'F': self.ReaumurFahrenheit(),
            'R': self.ReaumurRankine(), 'N': self.ReaumurNewton(), 'Ro': self.ReaumurRomer(), 
            'De': self.ReaumurDelisle()  
        }
        return int(calculo.get(self.op))
    
class RomerScale:

    def __init__(self, x, op) -> None:
        self.x = x
        self.op = op
        
    def RomerscaleCelsius(self):
        cel = (self.x - 7.5) * (40/21)
        return cel
    
    def RomerscaleKelvin(self):
        kel = ((self.x - 7.5) * (40/21)) + 273.15
        return kel
    
    def RomerscaleFahrenheit(self):
        fa = ((self.x - 7.5) * (24/7)) + 32
        return fa 
    
    def RomerscaleRankine(self):
        ra = ((self.x - 7.5) * (24/7)) + 491.67
        return ra
    
    def RomerscaleNewton(self):
        n = (self.x - 7.5) * (22/35)
        return n
    
    def RomerscaleReaumur(self):
        re = (self.x - 7.5) * (32/21)
        return re
    
    def RomerscaleDelisle(self):
        de = (60 - self.x) * (20/7)
        return de
    
    @property
    def operacao(self):
        calculo = {
            'C': self.RomerscaleCelsius(), 'K': self.RomerscaleKelvin(), 'F': self.RomerscaleFahrenheit(),
            'R': self.RomerscaleRankine(), 'N': self.RomerscaleNewton(), 'Re': self.RomerscaleReaumur(), 
            'De': self.RomerscaleDelisle()    
        }
        return int(calculo.get(self.op))
    
def convert_temp(temp, from_scale, to_scale):
    
    conversion_dict = {
        'C': Celsius(temp, to_scale), 'F': Fahrenheit(temp, to_scale), 'K': Kelvin(temp, to_scale),
        'R': Rankine(temp, to_scale), 'De': Delisle(temp, to_scale), 'N': Newton(temp, to_scale),
        'Re': Reaumur(temp, to_scale), 'Ro': RomerScale(temp, to_scale)
    }
    if from_scale != to_scale:
        result = conversion_dict.get(from_scale)
        return result.operacao
    return temp
print(convert_temp(-3.71, "R", "Re"))
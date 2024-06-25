class Horario:
    def __init__(self, h) -> None:
        self._h = h

    
    def __segundo(self, hora:str):
        s = hora.split(':')
        hora = int(s[0]) * 3600
        minuto = int(s[1]) * 60
        segundo = int(s[2]) + hora + minuto
        return segundo
    
    def __time(self, segundos):
        hora = segundos // 3600
        resto_segundos = segundos % 3600
        minutos = resto_segundos // 60
        segundos = resto_segundos % 60
        if hora == 24:
            hora = 0
   
        return f'{str(hora).zfill(2)}:{str(minutos).zfill(2)}:{str(segundos).zfill(2)}'
    
    def __add__(self, other):
        
        time_1 = self.__segundo(self._h)
        time_2 = self.__segundo(other._h)
        horario = time_1 + time_2
        horario_global = self.__segundo('24:00:00')
        if horario > horario_global:
            return self.__time(horario - horario_global)
        return self.__time(horario)

        
    def __sub__(self, other):
        time_1 = self.__segundo(self._h)
        time_2 = self.__segundo(other._h)
        horario = time_1 - time_2
        horario_global = self.__segundo('24:00:00')
        if horario < 0:
            return self.__time(horario + horario_global)
        return self.__time(horario)

def time_math(time1:str, op, time2:str):
   
    time_1 = Horario(time1)
    time_2 = Horario(time2)
    if op == '+': 
        return time_1 + time_2

    return time_1 - time_2



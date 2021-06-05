from cores import Cores
cores = Cores()

class Timer:
    def __init__(self, start):
        self.hours = start #Em horas absolutas
        self.minutes = 0
        self.days = 1

    def adicionar_tempo(self, time_passed):
        self.minutes += time_passed #SEMPRE EM MINUTOS! MUITO IMPORTANTE.
        while self.minutes >=60:
            self.hours += 1
            self.minutes -= 60
            while self.hours >= 24:
                self.days += 1
                self.hours -= 24
    
    def __str__(self):
        return f'AGORA SÃO {cores.redON}{self.hours:02d}:{self.minutes:02d}{cores.redOFF} DO {cores.redON}{self.days}°{cores.redOFF} DIA\n'






    
        
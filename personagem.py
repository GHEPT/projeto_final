from cores import Cores
from time import sleep
cores = Cores()


class Personagem:
    def __init__(self, score=0, stamina=100):
        self.stamina = 100
        self.score = 0
        self.nome = input('Digite o nome da sua CINDERELA: ').upper()
        self.arrumada = False
        self.pecas = 0
         
    def dormir(self):
        if self.stamina + 30 > 100:
            self.stamina = 100
        else:
            self.stamina += 30

    def pontuar(self, pontos):
        if self.score + pontos >= 100:
            self.score = 100
        elif self.score + pontos <= 0:
            self.score = 0
        else:
            self.score += pontos
        
    def mudar_stamina(self, pontos):
        if self.stamina + pontos >= 100:
            self.stamina = 100
        elif self.stamina + pontos <= 0:
            self.stamina = 0
        else:
            self.stamina += pontos
    
    def mostrar_personagem(self):
        print('\nSCORE')
        self.mostrarA = '|' * (int(self.score)//2) + '_' * (50 - (int(self.score)//2))
        for i in self.mostrarA:
            print(f'{cores.cyanON}'+i, end=""+f'{cores.cyanOFF}')
            sleep(.01)
        print(f' {cores.cyanON}{self.score}{cores.cyanOFF}')
        print(f'STAMINA')
        self.mostrarB = f'|' * (int(self.stamina)//2) + '_' * (50 - (int(self.stamina)//2))
        for i in self.mostrarB:
            print(f'{cores.greenON}'+i, end=""+f'{cores.greenOFF}')
            sleep(.01)
        print(f' {cores.greenON}{self.stamina}{cores.greenOFF}')

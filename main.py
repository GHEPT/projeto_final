from outras_opcoes import outras_opcoes
from random import randint
from mochila import Mochila
from personagem import Personagem
#from score import Score
from som import som
from timer import Timer
from outras_opcoes import outras_opcoes
import sys

mochila = Mochila()
relogio = Timer(8)
personagem = Personagem()
print('Jogo começou')
while True:
    escolha = input('Digite: ')
    if escolha == '1':
        som('beep')
        relogio.add_time(100)
    elif escolha == '2':
        mochila.adicionar('papel')
    elif escolha == '++':
        outras_opcoes()
    elif escolha == 'mochila':
        mochila.abrir()
    elif escolha == 'ver hora':
        print(relogio.clock())
    elif escolha == 'sair':
        sys.exit(0)
    else:
        print('Opção inexistente, tente outra vez.')


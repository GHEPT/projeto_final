from random import randint
from mochila import Mochila
from personagem import Personagem
from som import som
from timer import Timer
import sys

mochila = Mochila()
relogio = Timer(8)
personagem = Personagem()

# def outras_opcoes():
#     escolha_2 = input('Menu Sec: ')
#     if escolha_2 == 'mochila':
#         mochila.abrir()
#     elif escolha_2 == 'hora':
#         print(relogio.clock())
#     elif escolha_2 == 'score':
#         print(personagem.score)
#     elif escolha_2 == 'sair':
#         sys.exit(0)

###menu
    # elif escolha == '++':
    #     outras_opcoes()
    # elif escolha == 'mochila':
    #     outras_opcoes.mochila.abrir()
    # elif escolha == 'ver hora':
    #     print(relogio.clock())
####



print('Jogo começou')
while True:
    escolha = input('Digite: ')
    if escolha == '1':
        som('beep')
        relogio.adicionar_tempo(100)
    elif escolha == '2':
        mochila.adicionar('papel')

    elif escolha == 'sair':
        sys.exit(0)
    else:
        print('Opção inexistente, tente outra vez.')


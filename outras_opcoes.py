from personagem import Personagem
from mochila import Mochila
import sys
mochila = Mochila()
def outras_opcoes():
    escolha_2 = input('Menu Sec: ')
    if escolha_2 == 'mochila':
        mochila.abrir()
    elif escolha_2 == 'hora':
        print(relogio.clock())
    elif escolha_2 == 'score':
        personagem.score()
    elif escolha_2 == 'sair':
        sys.exit(0)
    
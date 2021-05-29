from random import randint
from mochila import Mochila
from personagem import Personagem
from som import som
from timer import Timer
import sys
from creditos import creditos

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


def consumir(item_da_mochila): #LISTAR OS POSSÍVEIS ITENS DA MOCHILA AQUI.
    if item_da_mochila in mochila.mochila:
        mochila.retirar(item_da_mochila)
        print(f'Você consumiu o item: {item_da_mochila}')
    if item_da_mochila == 'Papel':
        print('Você escreveu uma carta para o Príncipe. Ele adorou. Você aumentou o interesse do príncipe em você.')
    if item_da_mochila == 'Frasco Vermelho':
        print('Você fez um bolo e enviou para o príncipe.\nParece que não era suco concentrado de mirtilo. O príncipe passou mal. Você perdeu reputação.')
    else:
        print('Esse item não existe na mochila.')



        







print('Jogo começou')
while True:
    escolha = input('Digite: ').title()
    if escolha == '1':
        som('beep')
        relogio.adicionar_tempo(100)
    elif escolha == '2':
        mochila.adicionar('Frasco Vermelho')
    elif escolha == 'Consumir':
        item_da_mochila = input('Digite o nome do item que deseja consumir: ')
        consumir(item_da_mochila)
    elif escolha == 'Sair':
        creditos()
        sys.exit(0)
    else:
        print('Opção inexistente, tente outra vez.')


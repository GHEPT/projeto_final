from random import randint
from mochila import Mochila
#from personagem import Personagem
from som import som
from timer import Timer
import sys
#from creditos import creditos
from time import sleep
from principe import Principe
from falas import *

sonhos = 0
mochila = Mochila()
relogio = Timer(8)
#personagem = Personagem()
principe = Principe()

def consumir(item_da_mochila): #LISTAR OS POSSÍVEIS ITENS DA MOCHILA AQUI.
    if item_da_mochila in mochila.mochila:
        mochila.retirar(item_da_mochila)
        print(f'Você consumiu o item: {item_da_mochila}')
    if item_da_mochila == 'Papel':
        print('Você escreveu uma carta para o Príncipe. Ele adorou. Você aumentou o interesse do príncipe em você.')
        principe.amar(15)
    if item_da_mochila == 'Frasco Vermelho':
        print('Você fez um bolo e enviou para o príncipe.\nParece que não era suco concentrado de mirtilo. O príncipe passou mal. Você perdeu reputação.')
        principe.amar(-10)
    if item_da_mochila == 'Pêssego':
        print(f'A poção mágica favorita da fada madrinha é a de Pêssego! Ela amou e fez pra você o vestido mais lindo do Reino')
    else:
        print('Esse item não existe na mochila.')

def rng(): #Define um número aleatório entre 1 e 10. Sorte é variável global para uso em condições.
    global sorte
    sorte = randint(1,10)


if __name__ == '__main__':
    print()
    print('-=' * 50)
    soletrar(0, 5)
    opcao = input('Digite sua escolha: ')
    if opcao == '1':
        rng()
        if sorte < 5:
            print(falas[5])
            personagem.mudar_stamina(-25)
            relogio.adicionar_tempo(60)
            print(personagem)
            print(relogio)
        else:
            print(falas[6])
            principe.amar(3)
            relogio.adicionar_tempo(40)
            print(personagem)
            print(relogio)
    if opcao == '2':
        soletrar(7, 9)
        personagem.mudar_stamina(-5)
        relogio.adicionar_tempo(60)
        print(personagem)
        print(relogio)
        mochila.adicionar('Papel')
    if opcao == '3':
        som('varrendo')
        soletrar(9, 10)
        personagem.mudar_stamina(-25)
        relogio.adicionar_tempo(120)
        personagem.pontuar(35)
        print(personagem)
        print(relogio)
    if opcao == '4':
        som('cozinha')
        soletrar(10, 12)
        personagem.mudar_stamina(-20)
        relogio.adicionar_tempo(180)
        personagem.pontuar(30)
        mochila.adicionar('Frasco Vermelho')
        print(personagem)
        print(relogio)  
    soletrar(12, 13)
    for i in range(3):
        soletrar(13, 14)
        opcao = input('Digite sua escolha: ')
        if opcao == '1':
            rng()
            if sorte >= 8:
                soletrar(14, 15)
                personagem.mudar_stamina(-10)
                personagem.pontuar(30)
                relogio.adicionar_tempo(120)
                print(personagem)
                print(relogio)
            elif sorte > 4:
                soletrar(15, 16)
                personagem.mudar_stamina(-20)
                personagem.pontuar(30)
                relogio.adicionar_tempo(180)
                print(personagem)
                print(relogio)
            else:
                soletrar(16, 17)
                personagem.mudar_stamina(-30)
                personagem.pontuar(-20)
                relogio.adicionar_tempo(240)
                print(personagem)
                print(relogio)
        if opcao == '2':
            sonhos += 1
            if sonhos == 3:
                soletrar(19, 20)
                personagem.pontuar(-20)
                personagem.mudar_stamina(-5)
                relogio.adicionar_tempo(100)
                print(personagem)
                print(relogio)
            if sonhos == 2:
                soletrar(18, 19)
                principe.amar(20)
                personagem.mudar_stamina(5)
                personagem.pontuar(-5)
                relogio.adicionar_tempo(100)
                print(personagem)
                print(relogio)
            if sonhos == 1:
                soletrar(17, 18)
                personagem.mudar_stamina(5)
                personagem.pontuar(-5)
                relogio.adicionar_tempo(100)
                print(personagem)
                print(relogio)
        if opcao == '3':
            soletrar(20, 21)
        if opcao == '4':
            soletrar(20, 21)
        if opcao == '5':
            soletrar(20, 21)
    # nubia
    # edu
    soletrar(31, 35)
    relogio.hours = 12
    relogio.minutes = 0
    relogio.days = 3
    personagem.stamina = 0
    print(relogio)
    soletrar(35, 36)
    while True:
        opcao = input('Digite a opção [   ]: ')
        if opcao == '1':
                if relogio.hours <= 18:
                    relogio.adicionar_tempo(10)
                    print('Ainda não está na hora do Baile')
                else:
                    if personagem.stamina <= 40:
                        print(f'{personagem.nome} não tem energia suficiente para sair.')
                        relogio.adicionar_tempo(10)
                    else:
                        if 'Vestido' in mochila.mochila:
                            personagem.pontuar(50)
                            print(f'O vestido mais bonito da festa é o de {personagem.nome}. O interesse do príncipe por ela agora é de {principe.amor}. Eles se casaram e foram FELIZES PARA SEMPRE!')
                        else:
                            personagem.pontuar(-50)
                            print(f'{personagem.nome} foi para o baile sem vestido de gala. O príncipe não quis dançar com {personagem.nome}. FIM DE JOGO.')
        elif opcao == '2':
            if 'Pêssego' in mochila.mochila:
                print(f'A poção preferida da Fada Madrinha é a de Pêssego. Ela amou e fez o vestido mais incrível do Reino para {personagem.nome}. Agora você ainda precisa se arrumar')
                mochila.adicionar('Vestido')
                relogio.adicionar_tempo(120)
                personagem.mudar_stamina(30)
                mochila.retirar('Pêssego')
            else:
                print(f'{personagem.nome} ainda não colheu novos frutos para a poção. O que você está esperando?')
                relogio.adicionar_tempo(10)
        elif opcao == '3':
                mochila.adicionar('Pêssego')
                relogio.adicionar_tempo(30)
                personagem.mudar_stamina(20)
                print(f'Agora {personagem.nome} tem lindos pêssegos para usar. Ela fez o que gosta e ganhou 20 de STAMINA')
        elif opcao == '4':
            if 'Pêssego' in mochila:
                personagem.mudar_stamina(20)
                print(f'{personagem.nome} fez o que gosta e se alimentou. A STAMINA dela agora é {personagem.stamina}')
                mochila.retirar('Pêssego')
            else:
                personagem.mudar_stamina(-10)
                print(f'{personagem.nome} não tem o que comer ainda. Ela está faminta e a STAMINA baixou para {personagem.stamina}')
        elif opcao == '5':
            if personagem.arrumada:
                print(f'{personagem.nome} já está arrumada.')
            else:
                personagem.arrumada = True
                print(f'{personagem.nome} se preparou para ir ao baile! Será que {personagem.nome} tem tudo o que precisa?')
                personagem.mudar_stamina(30)
    
            




    
            


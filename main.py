from random import randint
from mochila import Mochila
from som import som
from timer import Timer
import sys
from time import sleep
from falas import *
from personagem import Personagem
sonhos = 0
enteada = 0
mochila = Mochila()
relogio = Timer(8)


def consumir(item_da_mochila): #LISTAR OS POSSÍVEIS ITENS DA MOCHILA AQUI.
    if item_da_mochila in mochila.mochila:
        mochila.retirar(item_da_mochila)
        print(f'{personagem.nome} consumiu o item: {item_da_mochila}.')
    if item_da_mochila == 'Papel':
        print(f'{personagem.nome} escreveu uma carta para o Príncipe. Ele adorou! Aumentou o interesse do príncipe em {personagem.nome}.')
        principe.amar(15)
    if item_da_mochila == 'Frasco Vermelho':
        print(f'{personagem.nome} fez um bolo e enviou para o príncipe.\nParece que não era suco concentrado de mirtilo. O príncipe passou mal. {personagem.nome} perdeu reputação.')
        principe.amar(-10)
    if item_da_mochila == 'Pêssego':
        print(f'A poção mágica favorita da fada madrinha é a de Pêssego! Ela amou e fez pra {personagem.nome} o vestido mais lindo do Reino.')
    else:
        pass


def rng(): #Define um número aleatório entre 1 e 10. Sorte é variável global para uso em condições.
    global sorte
    sorte = randint(1,10)


if __name__ == '__main__':
    print()
    print('-=' * 70)
    soletrar(72, 74)
    print('-=' * 70)
    personagem.mostrar_personagem()
    print(relogio)
    soletrar(0, 5)
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        som('carruagem_cidade')
        rng()
        if sorte < 5:
            soletrar(5, 6)
            personagem.mudar_stamina(-25)
            relogio.adicionar_tempo(120)
            personagem.mostrar_personagem()
            print(relogio)
        else:
            soletrar(6, 7)
            personagem.mudar_stamina(-25)
            principe.amar(3)
            relogio.adicionar_tempo(60)
            personagem.mostrar_personagem()
            print(relogio)
    if opcao == '2':
        soletrar(7, 9)
        personagem.mudar_stamina(-5)
        relogio.adicionar_tempo(60)
        mochila.adicionar('Papel')
        personagem.mostrar_personagem()
        print(relogio)
    if opcao == '3':
        som('varrendo')
        soletrar(9, 10)
        personagem.mudar_stamina(-25)
        relogio.adicionar_tempo(120)
        personagem.pontuar(35)
        personagem.mostrar_personagem()
        print(relogio)
    if opcao == '4':
        som('cozinha')
        soletrar(10, 11)
        personagem.mudar_stamina(-20)
        relogio.adicionar_tempo(180)
        personagem.pontuar(30)
        mochila.adicionar('Frasco Vermelho')
        personagem.mostrar_personagem()
        print(relogio)  
    soletrar(12, 13)
    for i in range(3):
        soletrar(13, 14)
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            rng()
            if sorte >= 7:
                soletrar(14, 15)
                personagem.mudar_stamina(-10)
                personagem.pontuar(30)
                relogio.adicionar_tempo(120)
                personagem.mostrar_personagem()
                print(relogio)
            elif sorte > 3:
                soletrar(15, 16)
                personagem.mudar_stamina(-20)
                personagem.pontuar(30)
                relogio.adicionar_tempo(180)
                personagem.mostrar_personagem()
                print(relogio)
            else:
                soletrar(16, 17)
                personagem.mudar_stamina(-30)
                personagem.pontuar(-20)
                relogio.adicionar_tempo(240)
                personagem.mostrar_personagem()
                print(relogio)
        elif opcao == '2':
            som('dormindo')
            sonhos += 1
            if sonhos == 3:
                soletrar(19, 20)
                personagem.pontuar(-20)
                personagem.mudar_stamina(-5)
                relogio.adicionar_tempo(100)
                personagem.mostrar_personagem()
                print(relogio)
            if sonhos == 2:
                soletrar(18, 19)
                principe.amar(20)
                personagem.mudar_stamina(5)
                personagem.pontuar(-5)
                relogio.adicionar_tempo(100)
                personagem.mostrar_personagem()
                print(relogio)
            if sonhos == 1:
                soletrar(17, 18)
                personagem.mudar_stamina(5)
                personagem.pontuar(-5)
                relogio.adicionar_tempo(100)
                personagem.mostrar_personagem()
                print(relogio)
        elif opcao == '3':
            enteada += 1
            if enteada == 1:
                soletrar(20, 21)
                personagem.pontuar(42)
                relogio.adicionar_tempo(120)
                personagem.mostrar_personagem()
                print(relogio)
            else:
                soletrar(69, 70)
                personagem.pontuar(-10)
                relogio.adicionar_tempo(60)
                personagem.mostrar_personagem()
                print(relogio)
        else:
            soletrar(70, 71)
# NOVAS PARTES DO MARCOS
    soletrar(59, 60)
    while True:
        soletrar(60, 61)
        if 'Papel' in mochila.mochila:
            soletrar(61, 62)
        if 'Frasco Vermelho' in mochila.mochila:
            soletrar(62, 63)         
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            soletrar(64, 65)#armário
            personagem.pecas += 1
            relogio.adicionar_tempo(50)
            personagem.mudar_stamina(-12)
            personagem.pontuar(10)
            personagem.mostrar_personagem()
            print(relogio)
        elif opcao =='2':
            soletrar(65, 66)#farda
            personagem.pecas += 1
            relogio.adicionar_tempo(70)
            personagem.pontuar(15)
            personagem.mudar_stamina(-13)
            personagem.mostrar_personagem()
            print(relogio)
        elif opcao == '3':
            soletrar(66, 67)#velhas
            relogio.adicionar_tempo(30)
            personagem.pontuar(-10)
            personagem.mudar_stamina(-8)
            personagem.mostrar_personagem()
            print(relogio)
        elif opcao == '4':
            soletrar(67, 68)#roubadas
            relogio.adicionar_tempo(40)
            personagem.pontuar(-10)
            personagem.mudar_stamina(-11)
            personagem.mostrar_personagem()
            print(relogio)
        elif opcao == '5':
            consumir('Papel')
            principe.amar(25)
            relogio.adicionar_tempo(60)
            personagem.mostrar_personagem()
            print(relogio)
        elif opcao == '6':
            consumir('Frasco Vermelho')
            principe.amar(-10)
            relogio.adicionar_tempo(120)
            personagem.mostrar_personagem()
            print(relogio)           
        else:
            opcao == '7'
            personagem.dormir()
            relogio.adicionar_tempo(240)
            break
        if personagem.pecas == 2:
            soletrar(71, 72)
            break
    personagem.dormir() #Esse dormir me quebrou... kk. Demorei a encontrar o o motivo da Stamina dela ter disparado de um dia para outro... É necessário passar uma informação pro usuário aqui sobre esse sono.
# PARTE DA NUBIA
    relogio.hours = 12
    relogio.minutes = 0
    relogio.days = 2
    soletrar(21, 22)
    personagem.mostrar_personagem()
    print(relogio)
    soletrar(22, 23)
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        relogio.adicionar_tempo(135)
        personagem.mudar_stamina(-15)
        soletrar(23, 24)
        personagem.mostrar_personagem()
        print(relogio)
        soletrar(74, 75)
        while True:
            if relogio.hours <= 19:
                soletrar(24, 25)
                opcao = input('Escolha uma opção: ')
                if opcao == '1':
                    soletrar(25, 26)
                    relogio.adicionar_tempo(120)
                    personagem.mudar_stamina(-15)
                    personagem.pontuar(35)
                    personagem.mostrar_personagem()
                    print(relogio)
                elif opcao == '2':
                    soletrar(26, 27)
                    relogio.adicionar_tempo(30)
                    personagem.mudar_stamina(-10)
                    personagem.pontuar(20)
                    personagem.mostrar_personagem()
                    print(relogio)
                elif opcao == '3':
                    rng()
                    if sorte > 5:
                        soletrar(27, 28)
                        relogio.adicionar_tempo(120)
                        personagem.mudar_stamina(-10)
                        personagem.pontuar(30)
                        personagem.mostrar_personagem()
                        print(relogio)
                    else: 
                        soletrar(28, 29)
                        relogio.adicionar_tempo(120)
                        personagem.mudar_stamina(-15)
                        personagem.pontuar(-30)
                        personagem.mostrar_personagem()
                        print(relogio)
                elif opcao == '4':
                    soletrar(29, 30)
                    relogio.adicionar_tempo(30)
                    personagem.mudar_stamina(20) 
                    personagem.mostrar_personagem()
                    print(relogio)
                elif opcao == '5':
                    soletrar(30, 31)
                    relogio.adicionar_tempo(47)
                    personagem.mostrar_personagem()
                    print(relogio)
            else:
                if relogio.hours > 19:
                    soletrar(31, 32)
                    break
                else:
                    print()
                    soletrar(32, 33)
                    personagem.pontuar(-20)
                    break
    if opcao == '2':
        soletrar(68, 69)
        relogio.adicionar_tempo(27)
        personagem.pontuar(23)
        personagem.mudar_stamina(-15)
        personagem.mostrar_personagem()
        print(relogio)
        while True:
            if relogio.hours <= 19:
                soletrar(33, 34)
                opcao = input('Escolha uma opção: ')
                if opcao == '1':
                    soletrar(34, 35)
                    relogio.adicionar_tempo(120)
                    personagem.mudar_stamina(-15)
                    personagem.pontuar(35)
                    personagem.mostrar_personagem()
                    print(relogio)
                elif opcao == '2':
                    soletrar(35, 36)
                    relogio.adicionar_tempo(30)
                    personagem.mudar_stamina(-10)
                    personagem.pontuar(20)
                    personagem.mostrar_personagem()
                    print(relogio)
                elif opcao == '3':
                    rng()
                    if sorte > 5:
                        soletrar(36, 37)
                        relogio.adicionar_tempo(120)
                        personagem.mudar_stamina(-10)
                        personagem.pontuar(30)
                        personagem.mostrar_personagem()
                        print(relogio)
                    else: 
                        soletrar(37, 38)
                        relogio.adicionar_tempo(120)
                        personagem.mudar_stamina(-15)
                        personagem.pontuar(-30)
                        personagem.mostrar_personagem()
                        print(relogio)
                elif opcao == '4':
                    soletrar(38, 39)
                    relogio.adicionar_tempo(30)
                    personagem.mudar_stamina(5)
                    personagem.mostrar_personagem()
                    print(relogio)
                elif opcao == '5':
                    soletrar(39, 40)
                    personagem.mudar_stamina(-5)
                    relogio.adicionar_tempo(34)
                    personagem.mostrar_personagem()
                    print(relogio)
                elif opcao == '6':
                    soletrar(40, 41)
                    relogio.adicionar_tempo(240)
                    personagem.mudar_stamina(-15)
                    personagem.mostrar_personagem()
                    print(relogio)
                elif opcao == '0':
                    break
            else:
                if relogio.hours == 19:
                    soletrar(41, 42)
                    break
                else:
                    soletrar(42, 43)
                    personagem.pontuar(-40)
                    relogio.adicionar_tempo(22)
                    personagem.mostrar_personagem()
                    print(relogio)
                    break
# PARTES DO EDU
    soletrar(43, 44)
    relogio.hours = 12
    relogio.minutes = 0
    relogio.days = 3
    personagem.stamina = 0
    personagem.score = 0
    soletrar(44, 47)
    personagem.mostrar_personagem()
    print(relogio)
    while True:
        soletrar(47, 48)
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            if relogio.hours < 18:#Se for menos de 18 horas não vai conseguir ir ao Baile
                relogio.adicionar_tempo(25)
                soletrar(48, 49)
                personagem.mostrar_personagem()
                print(relogio)
            elif relogio.hours >= 21:#Horário limite para ir ao Baile (21:10). Se passar disso o RNG mínimo somado ao relógio já vai ser mais de 22h.
                soletrar(82, 83)
                sys.exit(0)
            else:#Maior ou igual a 18 horas e a tempo de chegar no horário para o Baile, segue.
                if personagem.score < 40:#Pontuação (SCORE) menor que 40 acaba o jogo
                    soletrar(76, 77)
                elif personagem.score >= 40:#Maior ou igual a 40 pontos (SCORE), segue. 
                    if personagem.arrumada is False:#Se estiver desarrumada perde 15 pontos
                        soletrar(77, 78)
                        personagem.pontuar(-15)
                        if personagem.score < 40:#Se a pontuação for menor que 40, acaba o jogo mesmo indo ao Baile
                            soletrar(83, 84)
                            sys.exit(0)
                        else:#Se a pontuação mesmo penalizada for maior que 40, segue.
                            if 'Vestido' in mochila.mochila:#Se ela estiver com vestido na mochila, DÁ BOM, mas ela fecha o jogo com pontuação menor, pois não se arrumou.
                                principe.amar(10)
                                soletrar(50, 51)
                                rng()#Gerar randômico para decidir quanto tempo ela vai levar ara chegar ao Baile
                                if 1 <= sorte <= 4:#Se rand for entre 1 e 4
                                    relogio.adicionar_tempo(97)#Ea vai levar 1h37m pra chegar
                                    soletrar(84, 85)
                                    print(f'{personagem.nome} chegou às {cores.redON}{relogio.hours}:{relogio.minutes}{cores.redOFF} no Baile.\n')
                                    if relogio.hours >= 22:
                                        soletrar(82, 83)
                                        sys.exit(0)
                                    else:
                                        soletrar(78, 79)
                                        soletrar(79, 80)
                                        principe.amor += personagem.score // 2
                                        soletrar(80, 81)
                                        som('badalada')
                                        soletrar(81, 82)
                                        som('badalada')
                                        sys.exit(0)
                                elif 5 <= sorte <= 7:
                                    relogio.adicionar_tempo(72)#1h12
                                    soletrar(85, 86)
                                    print(f'{personagem.nome} chegou às {cores.redON}{relogio.hours}:{relogio.minutes}{cores.redOFF} no Baile.\n')
                                    if relogio.hours >= 22:
                                        soletrar(82, 83)
                                        sys.exit(0)
                                    else:
                                        soletrar(78, 79)
                                        soletrar(79, 80)
                                        principe.amor += personagem.score // 2
                                        soletrar(80, 81)
                                        som('badalada')
                                        soletrar(81, 82)
                                        som('badalada')
                                        sys.exit(0)
                                else:
                                    relogio.adicionar_tempo(51)#51min
                                    soletrar(86, 87)
                                    print(f'{personagem.nome} chegou às {cores.redON}{relogio.hours}:{relogio.minutes}{cores.redOFF} no Baile.\n')
                                    if relogio.hours >= 22:
                                        soletrar(82, 83)
                                        sys.exit(0)
                                    else:
                                        soletrar(78, 79)
                                        soletrar(79, 80)
                                        principe.amor += personagem.score // 2
                                        soletrar(80, 81)
                                        som('badalada')
                                        soletrar(81, 82)
                                        som('badalada')
                                        sys.exit(0)
                            else:#Se não estiver com vestido na mochila dá ruim, e acaba o jogo.
                                soletrar(51, 52)
                    else:#Se ela estiver arrumada, vem pra cá.
                        if 'Vestido' in mochila.mochila:#Se ela tiver vestido na mochila, DÁ BOM, e a pontuação é alta.
                            principe.amar(50)
                            soletrar(50, 51)
                            rng()#Gerar randômico para decidir quanto tempo ela vai levar ara chegar ao Baile
                            if 1 <= sorte <= 4:#Se rand for entre 1 e 4
                                relogio.adicionar_tempo(97)#Ea vai levar 1h37m pra chegar
                                soletrar(84, 85)
                                print(f'{personagem.nome} chegou às {cores.redON}{relogio.hours}:{relogio.minutes}{cores.redOFF} no Baile.\n')
                                if relogio.hours >= 22:
                                    soletrar(82, 83)
                                    sys.exit(0)
                                else:
                                    soletrar(78, 79)
                                    soletrar(79, 80)
                                    principe.amor += personagem.score // 2
                                    soletrar(80, 81)
                                    som('badalada')
                                    soletrar(81, 82)
                                    som('badalada')
                                    sys.exit(0)
                            elif 5 <= sorte <= 7:
                                relogio.adicionar_tempo(72)#1h12
                                soletrar(85, 86)
                                print(f'{personagem.nome} chegou às {cores.redON}{relogio.hours}:{relogio.minutes}{cores.redOFF} no Baile.\n')
                                if relogio.hours >= 22:
                                    soletrar(82, 83)
                                    sys.exit(0)
                                else:
                                    soletrar(78, 79)
                                    soletrar(79, 80)
                                    principe.amor += personagem.score // 2
                                    soletrar(80, 81)
                                    som('badalada')
                                    soletrar(81, 82)
                                    som('badalada')
                                    sys.exit(0)
                            else:
                                relogio.adicionar_tempo(51)#51min
                                soletrar(86, 87)
                                print(f'{personagem.nome} chegou às {cores.redON}{relogio.hours}:{relogio.minutes}{cores.redOFF} no Baile.\n')
                                if relogio.hours >= 22:
                                    soletrar(82, 83)
                                    sys.exit(0)
                                else:
                                    soletrar(78, 79)
                                    soletrar(79, 80)
                                    principe.amor += personagem.score // 2
                                    soletrar(80, 81)
                                    som('badalada')
                                    soletrar(81, 82)
                                    som('badalada')
                                    sys.exit(0)
                        else:#Se não estiver com vestido na mochila dá ruim, e acaba o jogo.
                            soletrar(51, 52)
        elif opcao == '2':
            if 'Pêssego' in mochila.mochila:
                soletrar(52, 53)
                mochila.adicionar('Vestido')
                relogio.adicionar_tempo(105)
                personagem.mudar_stamina(-25)
                personagem.pontuar(-34)
                mochila.retirar('Pêssego')
                personagem.mostrar_personagem()
                print(relogio)
            else:
                soletrar(53, 54)
                relogio.adicionar_tempo(28)
                personagem.mostrar_personagem()
                print(relogio)
        elif opcao == '3':
                relogio.adicionar_tempo(54)
                personagem.mudar_stamina(15)
                personagem.pontuar(18)
                soletrar(54, 55)
                mochila.adicionar('Pêssego')
                personagem.mostrar_personagem()
                print(relogio)
        elif opcao == '4':
            if 'Pêssego' in mochila.mochila:
                soletrar(55, 56)
                personagem.mudar_stamina(43)
                personagem.pontuar(47)
                mochila.retirar('Pêssego')
                relogio.adicionar_tempo(46)
                personagem.mostrar_personagem()
                print(relogio)
            else:
                soletrar(56, 57)
                personagem.mudar_stamina(-10)
                relogio.adicionar_tempo(27)
                personagem.mostrar_personagem()
                print(relogio)
        elif opcao == '5':
            if personagem.arrumada is True:
                soletrar(57, 58)
                personagem.mostrar_personagem()
                print(relogio)
            else:
                personagem.arrumada = True
                if relogio.hours < 18:
                    soletrar(75, 76)
                    personagem.pontuar(-21)
                    personagem.mudar_stamina(-17)
                    relogio.adicionar_tempo(120)
                    personagem.mostrar_personagem()
                    print(relogio)
                else:
                    soletrar(58, 59)
                    personagem.mudar_stamina(-17)
                    relogio.adicionar_tempo(120)
                    personagem.mostrar_personagem()
                    print(relogio)

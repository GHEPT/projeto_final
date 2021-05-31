from random import randint
from mochila import Mochila
#from personagem import Personagem
from som import som
from timer import Timer
import sys
#from creditos import creditos
from time import sleep
from falas import *

sonhos = 0
enteada = 0
mochila = Mochila()
relogio = Timer(8)
#personagem = Personagem()

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
        pass

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
            relogio.adicionar_tempo(120)
            print(personagem)
            print(relogio)
        else:
            print(falas[6])
            personagem.mudar_stamina(-25)
            principe.amar(3)
            relogio.adicionar_tempo(60)
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
            if sorte >= 7:
                soletrar(14, 15)
                personagem.mudar_stamina(-10)
                personagem.pontuar(30)
                relogio.adicionar_tempo(120)
                print(personagem)
                print(relogio)
            elif sorte > 3:
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
        elif opcao == '2':
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
        elif opcao == '3':
            enteada += 1
            if enteada == 1:
                soletrar(20, 21)
                personagem.pontuar(50)
                relogio.adicionar_tempo(120)
                print(personagem)
                print(relogio)
            else:
                soletrar(69, 70)
                personagem.pontuar(-10)
                relogio.adicionar_tempo(60)
                print(personagem)
                print(relogio)
        else:
            soletrar(70, 71)
    #novas partes do marcos
    #print(relogio)
    

    soletrar(59, 61)
    while True:
        if 'Papel' in mochila.mochila:
            soletrar(61, 62)
        if 'Frasco Vermelho' in mochila.mochila:
            soletrar(62, 63)         
        opcao = input('Digite a opção desejada: ')
        if opcao == '1':
            soletrar(64, 65)#armário
            personagem.pecas += 1
            relogio.adicionar_tempo(50)
            personagem.pontuar(10)
            print(relogio)
            print(personagem)
        elif opcao =='2':
            soletrar(65, 66)#farda
            personagem.pecas += 1
            relogio.adicionar_tempo(70)
            personagem.pontuar(20)
            print(relogio)
            print(personagem)
        elif opcao == '3':
            soletrar(66, 67)#velhas
            relogio.adicionar_tempo(30)
            personagem.pontuar(-10)
            print(relogio)
            print(personagem)
        elif opcao == '4':
            soletrar(67, 68)#roubadas
            relogio.adicionar_tempo(40)
            personagem.pontuar(-10)
            print(relogio)
            print(personagem)
        elif opcao == '5':
            consumir('Papel')
            principe.amar(25)
            relogio.adicionar_tempo(60)
            print(relogio)
            print(personagem)
        elif opcao == '6':
            consumir('Frasco Vermelho')
            principe.amar(-10)
            relogio.adicionar_tempo(120)
            print(relogio)
            print(personagem)           
        else:
            opcao == '7'
            personagem.dormir()
            relogio.adicionar_tempo(240)
            break
        if personagem.pecas == 2:
            soletrar(71, 72)
            break
    
    
    
    # nubia
    relogio.hours = 12
    relogio.minutes = 0
    relogio.days = 2
    soletrar(21, 22)
    soletrar(22, 23)

    opcao = input('Escolha uma opção [1 ou 2]: ')
    if opcao == '1':
        relogio.adicionar_tempo(240)
        personagem.mudar_stamina(-30)
        soletrar(23, 24)
        print(relogio)
        print(personagem)
        while True:
            if relogio.hours <= 21:
                print()
                soletrar(24, 25)
                opcao = input('Escolha uma opção [1 a 5]: ')
                if opcao == '1':
                    soletrar(25, 26)
                    relogio.adicionar_tempo(120)
                    personagem.mudar_stamina(-30)
                    personagem.pontuar(35)
                    print(personagem)
                    print(relogio)
                elif opcao == '2':
                    soletrar(26, 27)
                    relogio.adicionar_tempo(30)
                    personagem.mudar_stamina(-20)
                    personagem.pontuar(20)
                    print(personagem)
                    print(relogio)
                elif opcao == '3':
                    rng()
                    if sorte > 5:
                        soletrar(27, 28)
                        relogio.adicionar_tempo(120)
                        personagem.mudar_stamina(-30)
                        personagem.pontuar(30)
                        print(personagem)
                        print(relogio)
                    else: 
                        soletrar(28, 29)
                        relogio.adicionar_tempo(120)
                        personagem.mudar_stamina(-30)
                        personagem.pontuar(-30)
                        print(personagem)
                        print(relogio)
                elif opcao == '4':
                    soletrar(29, 30)
                    relogio.adicionar_tempo(30)
                    personagem.mudar_stamina(20) 
                    print(relogio)
                    print(personagem)
                elif opcao == '5':
                    soletrar(30, 31)
                    print(relogio)
                    print(personagem)
            else:
                if relogio.hours == 21:
                    soletrar(31, 32)
                    break
                else:
                    print()
                    soletrar(32, 33)
                    personagem.pontuar(-40)
                    break
    if opcao == '2':
        soletrar(68, 69)
        while True:
            if relogio.hours <= 19:
                print()
                soletrar(33, 34)
                opcao = input('Escolha uma opção [1 a 6]: ')
                if opcao == '1':
                    soletrar(34, 35)
                    relogio.adicionar_tempo(120)
                    personagem.mudar_stamina(-30)
                    personagem.pontuar(35)
                    print(relogio)
                elif opcao == '2':
                    soletrar(35, 36)
                    relogio.adicionar_tempo(30)
                    personagem.mudar_stamina(-20)
                    personagem.pontuar(20)
                    print(relogio)
                elif opcao == '3':
                    rng()
                    if sorte > 5:
                        soletrar(36, 37)
                        relogio.adicionar_tempo(120)
                        personagem.mudar_stamina(-30)
                        personagem.pontuar(30)
                        print(relogio)
                    else: 
                        soletrar(37, 38)
                        relogio.adicionar_tempo(120)
                        personagem.mudar_stamina(-30)
                        personagem.pontuar(-30)
                        print(relogio)
                elif opcao == '4':
                    soletrar(38, 39)
                    relogio.adicionar_tempo(30)
                    personagem.mudar_stamina(20) 
                elif opcao == '5':
                    soletrar(39, 40)
                elif opcao == '6':
                    relogio.adicionar_tempo(240)
                    personagem.mudar_stamina(-30)
                    soletrar(40, 41)
                elif opcao == '0':
                    break
            else:
                if relogio.hours == 19:
                    soletrar(41, 42)
                    break
                else:
                    print()
                    soletrar(42, 43)
                    personagem.pontuar(-40)
                    break
    # edu
    soletrar(43, 44)
    relogio.hours = 12
    relogio.minutes = 0
    relogio.days = 3
    personagem.stamina = 0
    print(relogio)
    soletrar(44, 47)
    while True:
        soletrar(47, 48)
        opcao = input('Digite a opção [1 a 5]: ')
        if opcao == '1':
            if relogio.hours < 18:
                relogio.adicionar_tempo(60)
                soletrar(48, 49)
                print(personagem)
                print(relogio)
            else:
                if 'Vestido' in mochila.mochila:
                    principe.amar(50)
                    soletrar(50, 51)
                    print(personagem)
                    print(relogio)
                else:
                    personagem.pontuar(-50)
                    soletrar(51, 52)
                    sys.exit(1)
                    break
        elif opcao == '2':
            if 'Pêssego' in mochila.mochila:
                soletrar(52, 53)
                mochila.adicionar('Vestido')
                relogio.adicionar_tempo(120)
                personagem.mudar_stamina(30)
                mochila.retirar('Pêssego')
                print(personagem)
                print(relogio)
            else:
                soletrar(53, 54)
                relogio.adicionar_tempo(10)
                print(personagem)
                print(relogio)
        elif opcao == '3':
                mochila.adicionar('Pêssego')
                relogio.adicionar_tempo(120)
                personagem.mudar_stamina(20)
                soletrar(54, 55)
                print(personagem)
                print(relogio)
        elif opcao == '4':
            if 'Pêssego' in mochila.mochila:
                personagem.mudar_stamina(20)
                soletrar(55, 56)
                mochila.retirar('Pêssego')
                relogio.adicionar_tempo(120)
                print(personagem)
                print(relogio)
            else:
                personagem.mudar_stamina(-10)
                relogio.adicionar_tempo(20)
                soletrar(56, 57)
                print(personagem)
                print(relogio)
        elif opcao == '5':
            if personagem.arrumada:
                soletrar(57, 58)
                print(personagem)
                print(relogio)
            else:
                personagem.arrumada = True
                soletrar(58, 59)
                personagem.mudar_stamina(30)
                relogio.adicionar_tempo(120)
                print(personagem)
                print(relogio)
                

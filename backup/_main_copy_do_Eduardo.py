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

def consumir(item_da_mochila): #LISTAR OS POSSÍVEIS ITENS DA MOCHILA AQUI.
    if item_da_mochila in mochila.mochila:
        mochila.retirar(item_da_mochila)
        print(f'Você consumiu o item: {item_da_mochila}')
    if item_da_mochila == 'Papel':
        print('Você escreveu uma carta para o Príncipe. Ele adorou.Você aumentou o interesse do príncipe em você.')
    if item_da_mochila == 'Frasco Vermelho':
        print('Você fez um bolo e enviou para o príncipe.\nParece que não era suco concentrado de mirtilo. O príncipe passou mal. Você perdeu reputação.')
    if item_da_mochila == 'Pêssego':
        return f'A poção mágica favorita da fada madrinha é a de Pêssego! Ela amou e fez pra você o vestido mais lindo do Reino'
    else:
        print('Esse item não existe na mochila.')

print()
print('-=' * 50)
soletrar(0, 1)

if __name__ == '__main__':
    mochila = Mochila()
    relogio = Timer(8)
    principe = Principe()
    #Código da Núbia e do Marcos
    #while True (Marcos)
    #while True (Núbia)
    relogio.hours = 12
    relogio.minutes = 0
    relogio.days = 3
    personagem.stamina = 0
    while True:
        print(relogio)
      
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
            if 'Pêssego' in mochila:
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
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
            relogio.adicionar_tempo(5)

import time
from personagem import Personagem
personagem = Personagem()
falas = [
    f'{personagem.nome} acorda com sua Madrasta gritando seu nome no andar inferior.', #0
    f'Ela olha ao redor, pássaros cantam para o lindo dia que se inicia.',#1
    f'Ao olhar pela janela, um grupo de homens se aproxima a cavalo. Suas primas correm na direção deles.',#2
    f'O que {personagem.nome} deve fazer agora?',#3
    f'OPÇÕES:\n[ 1 ] Correr para frente da casa e ver quem está chegando.\n[ 2 ] Cantar com os pássaros.\n[ 3 ] Ignorar a Madrasta e começar a varrer.\n[ 4 ] Correr e preparar o café da manhã da Madrasta.',#4
    f'Que azar! Sua Madrasta esperava por você no final da escada! Ela colocou o pé e você tropeçou. Stamina penalizada.',#5
    f'Você chega na frente do castelo e os homens já estão partindo. Mas um homem te nota e acena! É o príncipe! Parabéns! O interesse do príncipe aumentou.',#6
    f'Os pássaros fazem Tchaki Tchaki ao som da sua voz.',#7
    f'Um deles deixa cair um lindo pedaço de papel.',#8
    f'Sua Madrasta procura furiosa por você, mas se surpreende ao encontrá-la já trabalhando. Você pontuou.',#9
    f'Sua Madrasta parece extremamente satisfeita. Ela tira um Frasco Vermelho do vestido e te dá. \'Beba, minha filha. Esse suco é maravilhoso, você vai gostar.\'',#10
    f'Você adicionou Frasco Vermelho à mochila.',#11
    f'A rotina de {personagem.nome} é cansativa. Gerencie com cuidado seus afazeres. Você pode executar até 3 ações.',#12
    f'OPÇÕES:\n[ 1 ] Cuidar dos animais.\n[ 2 ] Tirar um cochilo.\n[ 3 ] Pegar água no poço.\n[ 4 ] Ajudar as primas a se arrumarem para o encontro com o príncipe.\n[ 5 ] Dar faxina.',#13
    f'*EVENTO DE SORTE* Você cuidou rapidamente de todos os bichos. Sua pontuação aumentou drasticamente.',#14
    f'Levou 3 horas para cuidar dos animais. Score aumentou.',#15
    f'*EVENTO CATASTRÓFICO* As galinhas fugiram e atrasaram seu dia! Sua pontuação foi penalizada.',#16
    f'Você sonhou com uma fada engraçada. Ela disse que te ajudaria a realizar o sonho de sua vida, mas você acordou antes dela terminar de falar. \nSerá que você consegue dormir novamente?',#17
    f'Você cochilou e voltou para o mesmo sonho. A fada disse que agora o príncipe está encantado por você.',#18
    f'Sua Madrasta te pega dormindo e te acorda com uma boa surra de vassoura! Pontuação gravemente penalizada.',#19
    f'Você adicionou água à sua mochila.',#20
    f'', #21
    f'', #22
    f'', #23
    f'', #24
    f'', #25
    f'', #26
    f'', #27
    f'', #28
    f'', #29
    f'', #30
    f'A madrasta diz que {personagem.nome} não poderá ir ao baile e rasga o seu vestido.', #31
    f'Todos foram e {personagem.nome} ficou sozinha em casa.',#32
    f'Triste, {personagem.nome} chorou muito e sua STAMINA é 0.',#33
    f'Ela precisa sair dessa fazendo o que gosta para ter STAMINA suficiente para ir ao Baile.',#34
    f'Você tem que ir para o baile até às 20:00.\nOPÇÕES:\n[ 1 ] Ir para o Baile\n[ 2 ] Fazer uma poção mágica\n[ 3 ] Pegar frutos no pomar\n[ 4 ] Comer\n[ 5 ] Se arrumar',#35
    f'Ainda não está na hora do baile.', #36

    

]


def soletrar(inicio, fim):
    for j in range(inicio, fim):
        # for letra in falas[j]:
        #     print(letra, end='', flush=True)
        #     time.sleep(0.05)
        # print()                
        # time.sleep(0.5)
        print(falas[j])



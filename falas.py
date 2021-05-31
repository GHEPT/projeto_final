import time
from personagem import Personagem
from principe import Principe
personagem = Personagem()
principe = Principe()
falas = [
    f'{personagem.nome} acorda com sua Madrasta gritando seu nome no andar inferior.', #0
    f'Ela olha ao redor, pássaros cantam para o lindo dia que se inicia.',#1
    f'Ao olhar pela janela, um grupo de homens se aproxima a cavalo. Suas primas correm na direção deles.',#2
    f'O que {personagem.nome} deve fazer agora?',#3
    f'OPÇÕES:\n[ 1 ] Correr para frente da casa e ver quem está chegando.\n[ 2 ] Cantar com os pássaros.\n[ 3 ] Ignorar a Madrasta e começar a varrer.\n[ 4 ] Correr e preparar o café da manhã da Madrasta.',#4
    f'Que azar! Sua Madrasta esperava por você no final da escada! Ela colocou o pé e você tropeçou. Stamina penalizada.',#5
    f'Você chega na frente do castelo e os homens já estão partindo. Mas um homem te nota e acena! É o príncipe! Parabéns! O interesse do príncipe aumentou.',#6
    f'Os pássaros dançam ao som da sua voz.',#7
    f'Um deles deixa um lindo pedaço de papel.',#8
    f'Sua Madrasta procura furiosa por você, mas se surpreende ao encontrá-la já trabalhando. Você pontuou.',#9
    f'Sua Madrasta parece extremamente satisfeita. Ela tira um Frasco Vermelho do vestido e te dá.',#10
    f'Você pega o item com desconfiança.',#11
    f'{personagem.nome} inicia sua rotina. Gerencie com cuidado seus afazeres. Você pode executar até 3 ações.',#12
    f'OPÇÕES:\n[ 1 ] Cuidar dos animais.\n[ 2 ] Tirar um cochilo.\n[ 3 ] Ajudar as enteadas a se arrumarem para o encontro com o príncipe.',#13
    f'*EVENTO DE SORTE* Você cuidou rapidamente de todos os bichos. Sua pontuação aumentou drasticamente.',#14
    f'Levou 3 horas para cuidar dos animais. Score aumentou.',#15
    f'*EVENTO CATASTRÓFICO* As galinhas fugiram e atrasaram seu dia! Sua pontuação foi penalizada.',#16
    f'Você sonhou com uma fada engraçada. Ela disse que te ajudaria a realizar o sonho de sua vida, mas você acordou antes dela terminar de falar. \nSerá que você consegue dormir novamente?',#17
    f'Você cochilou e voltou para o mesmo sonho. A fada disse que agora o príncipe está encantado por você.',#18
    f'Sua Madrasta te pega dormindo e te acorda com uma boa surra de vassoura! Pontuação gravemente penalizada.',#19
    f'Passar horas com as enteadas valeu a pena: Você descobriu que haverá um baile com o príncipe.',#20
    f'''As fortes batidas na porta fazem {personagem.nome} acordar assustada. É a Madrasta fazendo novas exigências para o dia antes de sair de casa.
    ''',#21
    f'''  
    O número de tarefas aumentam. É necessário arrumar e limpar a casa para a festa que a Madrasta dará as 21:00.\n
    Além disso, {personagem.nome} ainda precisa fazer os retoques finais em seu vestido para o baile.\n
    O que deseja fazer?

    [ 1 ] Aproveita que a madrasta e as primas sairam para começar os retoques finais no vestido, deixando as tarefas para depois.
    [ 2 ] Conhecendo a madrasta que tem e com o desejo de ganhar a sua simpatia, corre para fazer o que pediu e deixa o vestido para depois.
''',#22
    f'Oh, que maravilha! Com a ajuda dos pequenos animais que tem como amigos os retoques finais ficaram ótimos. Ainda não é o ideal para um baile, mas é um ótimo começo. \nEntretanto, {personagem.nome} se distraiu tanto que não viu a hora passar, agora tem menos tempo para fazer tudo!',#23
    f'''É hora de focar nas atividades da casa. O que gostaria de fazer?
    [ 1 ] Varrer a casa e limpar os móveis
    [ 2 ] Lavar as louças
    [ 3 ] Preparar as refeições para servir os convidados
    [ 4 ] Pausa para comer
    [ 5 ] Arrumar a mesa
    ''',#24
    f'Você limpou a casa e ela se encontra impecável novamente, os convidados ficarão impressinados e sua Madrasta satisfeita com o resultado!',#25
    f'Finalmente uma cozinha decente! Como pode poucas pessoas sujarem tanta coisa em tão pouco tempo?',#26
    f'A refeição parece divina! O aroma pode ser sentido de longe. Será um sucesso!',#27
    f'É um desastre! Você se distraiu cantando com os pássaros na janela e o prato principal queimou! Se prepare para a fúria ou torça para nem repararem.',#28
    f'A fome era maior do que poderia aguentar e uma pausa era necessária. Torça para isso não interferir no resultado final.',#29
    f'Mesa finalizada! Para você parece terrível, mas é o jeito estranho como a Madrasta gosta que fique. Tudo para agradá-la, certo?',#30
    f'Ela chegou! Não é o cenário perfeito, mas pelo menos não está um completo desastre. O serviço agora é na festa, assim que acabar o descanso merecido chegará.',#31
    f'Sua Madrasta chegou enquanto você ainda fazia as tarefas, isso é um desastre! Os convidados chegaram enquanto você organizava e sua pontuação com ela caiu.',#32
    f'''O que gostaria de fazer?
    [ 1 ] Varrer a casa e limpar os móveis
    [ 2 ] Lavar as louças
    [ 3 ] Preparar as refeições para servir os convidados
    [ 4 ] Pausa para comer
    [ 5 ] Arrumar a mesa
    [ 6 ] Fazer ajustes no vestido
    ''',#33
    f'Você limpou a casa e ela se encontra impecável novamente! Aumento na pontuação',#34
    f'Finalmente uma cozinha decente! Como pode poucas pessoas sujarem tanta coisa em tão pouco tempo? Aumento na pontuação',#35
    f'A refeição parece divina! O aroma pode ser sentido de longe. Será um sucesso!',#36
    f'É um desastre! {personagem.nome} se distraiu cantando com os pássaros na janela e o prato principal queimou! Pontuação penalizada.',#37
    f'A fome de {personagem.nome} era maior do que poderia aguentar e uma pausa era necessária.',#38
    f'Mesa finalizada! Para {personagem.nome} parece terrível, mas é o jeito como a Madrasta gosta que fique. Tudo para agradá-la, certo?',#39
    f'Oh, que maravilha! Com a ajuda dos pequenos animais que tem como amigos os retoques finais ficaram ótimos. Ainda não é o ideal para um baile, mas é um ótimo começo.',#40
    f'A Madrasta chegou! Não é o cenário perfeito, mas pelo menos não está um completo desastre. O descanso merecido chegou.\nEste é o final do segundo dia. Você tem um vestido para o baile.',#41
    f'A Madrasta chegou enquanto {personagem.nome} ainda fazia as tarefas, isso é um desastre! Os convidados chegaram enquanto {personagem.nome} organizava e sua pontuação com ela caiu.\nEste é o final do segundo dia. Você tem um vestido para o baile.',#42
    f'A madrasta diz que {personagem.nome} não poderá ir ao baile e rasga o seu vestido.',#43
    f'Todos foram e {personagem.nome} ficou sozinha em casa.',#44
    f'Triste, {personagem.nome} chorou muito e sua STAMINA é 0.',#45
    f'{personagem.nome} precisa sair dessa fazendo o que gosta para ter STAMINA suficiente para ir ao Baile.',#46
    f'{personagem.nome} tem que ir para o baile até às 18:00.\nOPÇÕES:\n[ 1 ] Ir para o Baile\n[ 2 ] Fazer uma poção mágica\n[ 3 ] Pegar frutos no pomar\n[ 4 ] Comer\n[ 5 ] Se arrumar',#47
    f'Ainda não está na hora do Baile',#48
    f'{personagem.nome} não tem energia suficiente para sair.',#49
    f'O vestido mais bonito da festa é o de {personagem.nome}. O amor do príncipe aumentou.',#50
    f'{personagem.nome} foi para o baile sem o Vestido Mágico. O príncipe não quis dançar com {personagem.nome}. FIM DE JOGO.',#51
    f'A poção preferida da Fada Madrinha é a de Pêssego. Ela amou e fez o vestido mais incrível do Reino para {personagem.nome}. Agora você ainda precisa se arrumar',#52
    f'{personagem.nome} ainda não colheu novos frutos para a poção. O que você está esperando?',#53
    f'Agora {personagem.nome} tem lindos pêssegos para usar. Ela fez o que gosta e ganhou 20 de STAMINA',#54
    f'{personagem.nome} fez o que gosta e se alimentou. A STAMINA dela subiu.',#55
    f'{personagem.nome} não tem o que comer ainda. Ela está faminta e a STAMINA baixou.',#56
    f'{personagem.nome} já está arrumada.',#57
    f'{personagem.nome} se preparou para ir ao baile! Será que {personagem.nome} tem tudo o que precisa?',#58 
    #novas linhas do marcos
    f'{personagem.nome} terminou todos os afazeres. Agora resta procurar por materiais que sirvam para fazer um vestido! Encontre um tecido útil e uma renda adequada.',#59
    f'[ 1 ] Se arriscar e verificar o armário da Madrasta.\n[ 2 ] Verificar no porão.\n[ 3 ] Desmanchar roupas velhas.\n[ 4 ] Roubar do varal da vizinha.', #60
    f'[ 5 ] Usar o papel na mochila e escrever Carta para o príncipe',#61
    f'[ 6 ] Frasco Vermelho e fazer um bolo de mirtilo.',#62
    f'[ 7 ] Dormir.',#63
    f'Quem não arrisca não petisca. Você encontrou um pedaço de renda para enfeitar seu vestido.',#64
    f'Você encontra fardas velhas de seu falecido pai e as reaproveita como tecido.',#65
    f'Suas enteadas não aceitam doar roupas para você. E você não tem peças sobressalentes.',#66
    f'{personagem.nome} vai até o varal da vizinha, mas ela percebe suas intenções e corre atrás de você com um chinelo.', #67
    f'\nÉ hora de focar nas atividades da casa. Não esqueça de trabalhar no seu vestido.',#68
    f'Suas enteadas não precisam mais de ajuda. Pare de de perder tempo.', #69
    f'Opção Incorreta. Pare de perder tempo.',#70
    f'Você encontrou todas as peças as tempo.\nVestido Rudimentar foi adicionado à mochila.',#71

]


def soletrar(inicio, fim):
    for j in range(inicio, fim):
        # for letra in falas[j]:
        #     print(letra, end='', flush=True)
        #     time.sleep(0.05)
        # print()                
        # time.sleep(0.5)
        print(falas[j])




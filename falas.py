import time
from personagem import Personagem
from principe import Principe
from mochila import Mochila
mochila = Mochila()
personagem = Personagem()
principe = Principe()
from cores import Cores
cores = Cores()

falas = [
    f'PRIMEIRO DIA\n\n{personagem.nome} acorda com sua madrasta gritando seu nome no andar inferior.',#0
    f'Ela olha ao redor, pássaros cantam para o lindo dia que se inicia.',#1
    f'Ao olhar pela janela, um grupo de homens se aproxima a cavalo. Suas primas correm na direção deles.',#2
    f'O que {personagem.nome} deve fazer agora?\n',#3
    f'OPÇÕES:\n[ 1 ] Correr para frente da casa e ver quem está chegando.\n[ 2 ] Cantar com os pássaros.\n[ 3 ] Ignorar a madrasta e começar a varrer.\n[ 4 ] Correr e preparar o café da manhã da madrasta.',#4
    f'Que azar! A madrasta esperava por {personagem.nome} no final da escada! Ela colocou o pé e {personagem.nome} tropeçou. STAMINA penalizada.',#5
    f'{personagem.nome} chega na frente do castelo e os homens já estão partindo. Mas um homem a percebe e acena! É o príncipe, parabéns! O interesse do príncipe aumentou, mas seu SCORE com a madrasta não.',#6
    f'Os pássaros dançam ao som da voz de {personagem.nome}.',#7
    f'Um deles deixa um lindo pedaço de papel.',#8
    f'A madrasta procura furiosa por {personagem.nome}, mas se surpreende ao encontrá-la já trabalhando. Ponto!',#9
    f'A madrasta parece extremamente satisfeita.\nEla tira um {cores.redON}Frasco Vermelho{cores.redOFF} do vestido e dá para {personagem.nome}, que o pega com desconfiança.',#10
    f'Ela pega o item com desconfiança.',#11
    f'{personagem.nome} inicia sua rotina e precisa gerenciar com cuidado seus afazeres.\nEla pode executar até 3 ações.\n',#12
    f'OPÇÕES:\n[ 1 ] Cuidar dos animais.\n[ 2 ] Tirar um cochilo.\n[ 3 ] Ajudar as primas a se arrumarem para o encontro com o príncipe.',#13
    f'*EVENTO DE SORTE* Ela cuidou rapidamente de todos os bichos. A pontuação dela aumentou significativamente.',#14
    f'{personagem.nome} levou 3 horas para cuidar dos animais. A pontuação dela aumentou.',#15
    f'*EVENTO CATASTRÓFICO* As galinhas fugiram e atrasaram o dia de {personagem.nome}! Sua pontuação foi penalizada.',#16
    f'{personagem.nome} sonhou com uma fada engraçada.\nEla disse que a ajudaria a realizar o sonho da vida dela, mas {personagem.nome} acordou antes que ela terminasse de falar.\nSerá que {personagem.nome} pode dormir novamente?',#17
    f'{personagem.nome} cochilou e voltou para o mesmo sonho. A fada disse que o príncipe está encantado por ela.',#18
    f'A madrasta de {personagem.nome} lhe pega dormindo e lhe acorda com uma boa surra de vassoura! Pontuação gravemente penalizada.\n',#19
    f'Passar horas com as primas valeu a pena: {personagem.nome} descobriu que haverá um baile com o príncipe.',#20
    f'SEGUNDO DIA\n\nAs fortes batidas na porta fazem {personagem.nome} acordar assustada.\nÉ a madrasta fazendo novas exigências para o dia antes de sair de casa.\nApesar do sono dessa noite, com o susto a STAMINA subiu apenas 30.',#21
    f'O número de tarefas aumenta.\nÉ necessário arrumar e limpar a casa para a festa que a Madrasta dará as 19:00.\nAlém disso, {personagem.nome} ainda precisa fazer os retoques finais em seu vestido para o baile.\n\nO que ela deve fazer?\n[ 1 ] Aproveitar que a madrasta e as primas sairam para começar os retoques finais no vestido, deixando as tarefas para depois.\n[ 2 ] Conhecendo a madrasta que tem e com o desejo de ganhar a sua simpatia, ela deve correr para fazer o que pediu e deixa o vestido para depois.',#22
    f'Oh, que maravilha! Com a ajuda dos pequenos animais que tem como amigos os retoques finais ficaram ótimos.\nAinda não é o ideal para um baile, mas é um ótimo começo.\nEntretanto, {personagem.nome} se distraiu tanto que não viu a hora passar e agora tem menos tempo para fazer tudo!',#23
    f'O que ela deve fazer?\n[ 1 ] Varrer a casa e limpar os móveis\n[ 2 ] Lavar as louças\n[ 3 ] Preparar as refeições para servir os convidados\n[ 4 ] Pausa para comer\n[ 5 ] Arrumar a mesa',#24
    f'{personagem.nome} limpou a casa e a deixou impecável novamente.\nOs convidados ficarão impressinados e sua madrasta satisfeita com o resultado!',#25
    f'Finalmente uma cozinha decente!\nComo pode poucas pessoas sujarem tanta coisa em tão pouco tempo?',#26
    f'A refeição parece divina!\nO aroma pode ser sentido de longe. Será um sucesso!',#27
    f'É um desastre!\n{personagem.nome} se distraiu cantando com os pássaros na janela e o prato principal queimou!\nEla precisa se preparar para a fúria da madrasta ou torcer para nem repararem.',#28
    f'A fome era maior do que poderia aguentar e uma pausa era necessária.\nEla deve torcer para isso não interferir no resultado final.',#29
    f'Mesa finalizada!\nPara {personagem.nome} parece terrível, mas é o jeito estranho como a madrasta gosta que fique.\nTudo para agradá-la, certo?',#30
    f'Ela chegou!\nNão é o cenário perfeito, mas pelo menos não está um completo desastre.\nO serviço agora é na festa! Assim que acabar, o descanso merecido chegará.\nEste é o FIM DO SEGUNDO DIA e {personagem.nome} tem um vestido para o baile.\n',#31
    f'A madrasta chegou enquanto {personagem.nome} ainda fazia as tarefas.\nIsso é um desastre! Os convidados chegaram enquanto ela organizava e a pontuação dela caiu.',#32
    f'''O que {personagem.nome} deve fazer?
[ 1 ] Varrer a casa e limpar os móveis
[ 2 ] Lavar as louças
[ 3 ] Preparar as refeições para servir os convidados
[ 4 ] Pausa para comer
[ 5 ] Arrumar a mesa
[ 6 ] Fazer ajustes no vestido''',#33
    f'{personagem.nome} limpou a casa e a deixou impecável novamente!\nAumento na pontuação!',#34
    f'Finalmente uma cozinha decente!\nComo pode poucas pessoas sujarem tanta coisa em tão pouco tempo?',#35
    f'A refeição parece divina!\nO aroma pode ser sentido de longe. Será um sucesso!',#36
    f'É um desastre! {personagem.nome} se distraiu cantando com os pássaros na janela e o prato principal queimou! Pontuação penalizada.',#37
    f'A fome de {personagem.nome} era maior do que ela poderia aguentar e uma pausa era necessária.',#38
    f'Mesa finalizada!\nPara {personagem.nome} parece terrível, mas é o jeito como a madrasta gosta que fique.\nTudo para agradá-la, certo?',#39
    f'Oh, que maravilha!\nCom a ajuda dos pequenos animais que tem como amigos os retoques finais ficaram ótimos.\nAinda não é o ideal para um baile, mas é um ótimo começo.',#40
    f'A madrasta chegou!\nNão é o cenário perfeito, mas pelo menos não está um completo desastre. O descanso merecido chegou.\nEste é o FIM DO SEGUNDO DIA. {personagem.nome} tem um vestido para o baile.\n',#41
    f'Os convidados chegaram enquanto {personagem.nome} organizava e sua pontuação com a madrasta caiu.\nEste é o FIM DO SEGUNDO DIA e {personagem.nome} tem um vestido para o baile.',#42
    f'TERCEIRO DIA\n\nDecidida a impedir que {personagem.nome} vá ao baile a madrasta RASGA O SEU VESTIDO!',#43
    f'{personagem.nome} ficou desolada e chorou muito. Sua STAMINA e seu SCORE zeraram!',#44
    f'Enquanto a madrasta e suas primas se preparam, {personagem.nome} precisa conseguir outro vestido sem que ninguém descubra.',#45
    f'A STAMINA e o SCORE de {personagem.nome} serão decisivos para o sucesso dela.',#46
    f'{cores.yellowON}ATENÇÃO{cores.yellowOFF}\n| {personagem.nome} só poderá ir para o Baile quando todos saírem, após às 18:00.\n| Ela precisa chegar no Baile até 22:00, horário da dança com o príncipe.\n| Leva EM TORNO de 1 hora para chegar ao Baile.\n\nOPÇÕES:\n[ 1 ] Ir para o Baile\n[ 2 ] Fazer uma poção mágica\n[ 3 ] Pegar frutos no pomar\n[ 4 ] Comer\n[ 5 ] Se arrumar',#47
    f'{personagem.nome} ainda não pode ir ao Baile.',#48
    f'{personagem.nome} não tem energia suficiente para sair.',#49
    f'{personagem.nome} está com o vestido mais bonito da festa!',#50
    f'NÃO É POSSÍVEL! {personagem.nome} foi para o baile sem o Vestido Mágico!\nO príncipe não quis dançar com {personagem.nome} e ela não conseguiu se casar!\nFIM DE JOGO.\n',#51
    f'A poção preferida da Fada Madrinha é a de Pêssego!\nEla amou e fez o {cores.magentaON}vestido{cores.magentaOFF} mais incrível do Reino para {personagem.nome}.\nMas, a euforia foi tanta que a madrasta se incomodou e {personagem.nome} perdeu pontos.',#52
    f'{personagem.nome} enfia a mão no fundo da mochila mas não encontra nada.\nA mochila está vazia e ela não tem ingrediente para a poção mágica.',#53
    f'O pomar estava carregado! Agora {personagem.nome} tem lindos pêssegos para usar. Ela está desfarçando bem!',#54
    f'{personagem.nome} se alimentou e está agindo com naturalidade.\nMas, ela tem ingrediente para a poção mágica?',#55
    f'{personagem.nome} enfia a mão no fundo da mochila mas não encontra nada.\nA mochila está vazia e ela não tem o que comer ainda.',#56
    f'{personagem.nome} já se arrumou para o Baile! Já está tudo pronto para ir?',#57
    f'{personagem.nome} se produziu toda para ir ao Baile e ficou incrível!\nSerá que ela tem tudo o que precisa para esse momento mágico?',#58 
    #novas linhas do marcos
    f'Ahhh... {personagem.nome} já fez as três escolhas. Tudo bem! Bora procurar por materiais que sirvam para fazer um vestido!\nEla deve encontrar um tecido útil [E] uma renda adequada.\n',#59
    f'OPÇÕES:\n[ 1 ] Se arriscar e verificar o armário da madrasta.\n[ 2 ] Verificar no porão.\n[ 3 ] Desmanchar roupas velhas.\n[ 4 ] Roubar do varal da vizinha.', #60
    f'[ 5 ] Usar o papel na mochila e escrever carta para o príncipe',#61
    f'[ 6 ] Usar o {cores.redON}Frasco Vermelho{cores.redOFF} e fazer um bolo de mirtilo.',#62
    f'[ 7 ] Dormir.',#63
    f'Quem não arrisca não petisca!\n{personagem.nome} encontrou um lindo pedaço de renda para enfeitar seu vestido.',#64
    f'{personagem.nome} encontra fardas velhas de seu falecido pai e as reaproveita como belos detalhes para o vestido.',#65
    f'As primas de {personagem.nome} não aceitam doar roupas e ela não tem peças suficientes...',#66
    f'{personagem.nome} vai até o varal da vizinha, mas ela percebe suas intenções e corre atrás dela com um chinelo.\nSTAMINA comprometida.', #67
    f'Agradar a madrasta lhe rendeu pontos.\nÉ hora de focar nas atividades da casa. {personagem.nome} não pode esquecer de trabalhar em seu vestido.',#68
    f'As primas não precisam mais de ajuda.\n{personagem.nome} está perdendo tempo!!', #69
    f'Opção Incorreta.\n{personagem.nome}, pare de perder tempo...',#70
    f'SHOW! {personagem.nome} encontrou todas as peças a tempo.\nUm {cores.magentaON}Vestido Rudimentar{cores.magentaOFF} foi adicionado à mochila.\nEste é o FIM DO PRIMEIRO DIA!\n',#71
    f'\nE N R E D O\n\n{personagem.nome} é uma jovem muito bela que se tornou serviçal de sua madrasta malvada desde que seu pai morreu.\nA chance de se tornar livre é se casar com o príncipe caso consiga conquistá-lo no baile que o Rei realizará para escolher uma esposa para o seu filho.',#72
    f'\nPara isso, ela deve realizar algumas tarefas, conquistando a simpatia da madrasta nos próximos {cores.redON}3 DIAS{cores.redOFF} aumentando a sua PONTUAÇÃO.\nO príncipe já ouviu falar de sua beleza e está querendo muito conhecê-la, mas cuidado, ele pode perder o interesse.\n',#73
    f'É hora de focar nas atividades da casa.',#74
    f'{personagem.nome} se produziu toda para ir ao Baile e ficou incrível!\nO problema é que a madrasta ainda está em casa e ficou muito desconfiada.\nIsso compromete o seu SCORE.',#75
    f'A pontuação de {personagem.nome} não é suficiente para avançar! Será que dá tempo de reverter?',#76
    f'Apesar de estar com um lindo vestido, o príncipe percebeu que você não se preparou para o Baile.\n{personagem.nome} perdeu {cores.redON}15{cores.redOFF} em SCORE.',#77
    f'A PONTUAÇÃO de {personagem.nome} foi [ {personagem.score} ]\nO príncipe admira sua jornada e metade dos pontos de {personagem.nome} foram convertidos em AMOR.',#78
    f'Agora o interesse do príncipe é [ {principe.amor} ]',#79
    f'{personagem.nome} participou do baile com o príncipe e antes que o encanto se desfizesse {personagem.nome} entrou na carruagem pronta para partir.',#80
    f'O príncipe entrou na carruagem com {personagem.nome} e eles foram FELIZES PARA SEMPRE!\n',#81
    f'Infelizmente {personagem.nome} chegou tarde demais no baile e o príncipe já escolheu seu par.\nFIM DE JOGO.\n',#82
    f'O SCORE de {personagem.nome} ficou abaixo de 40.\nInfelizmente {personagem.nome} não conseguiu conquistar o príncipe. FIM DE JOGO!',#83
    f'O percurso foi de {cores.redON}1 hora e 37 minutos{cores.redOFF}.',#84
    f'O percurso foi de {cores.yellowON}1 hora e 12 minutos{cores.yellowOFF}.',#85
    f'O percurso foi de {cores.greenON}51 minutos{cores.greenOFF}.',#86
    ]


def soletrar(inicio, fim):
    for j in range(inicio, fim):
        for letra in falas[j]:
            print(letra, end='', flush=True)
            time.sleep(0.02)
        print()                
        time.sleep(0.2)




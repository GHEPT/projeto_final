import time
from personagem import Personagem
personagem = Personagem()
falas = [
    #FALAS DO INÍCIO DO PROGRAMA
    f'\n{personagem.nome} é uma jovem muito bela que se tornou serviçal de sua madrasta malvada desde que seu pai morreu.\nSua chance de se tornar livre está em conseguir ir ao baile que o Rei realizará para escolher a esposa para seu filho.', #0
    '\nPara isso, ela deve realizar algumas tarefas, conquistando a simpatia da madrasta aumentando o seu SCORE.\nO príncipe já ouviu falar de sua beleza e está querendo muito conhecê-la. Mas, cuidado, ele pode perder o interesse fácil caso sua STAMINA esteja baixa.', #1

    #FALAS DO DIA3
    f'\nA madrasta diz que {personagem.nome} não poderá ir ao baile e rasga o seu vestido. Todos foram e {personagem.nome} ficou sozinha em casa.\nTriste, {personagem.nome} chorou muito e sua STAMINA é 0.\nEla precisa sair dessa fazendo o que gosta para ter STAMINA suficiente para ir ao Baile.'
]

def soletrar(inicio, fim):
    for j in range(inicio, fim):
        for letra in falas[j]:
            print(letra, end='')
            time.sleep(0.05)
        print()                
        time.sleep(0.5)


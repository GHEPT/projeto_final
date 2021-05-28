import winsound


faixas = {
    'beep': 'button-32.wav',
}


def som(faixa):
    musica = faixas[faixa]
    winsound.PlaySound(musica, winsound.SND_FILENAME)
    print('sound played')  

import winsound


faixas = {
    'beep': 'som\\button-32.wav',
    'badalada': 'som\\badalada.wav'
}


def som(faixa):
    musica = faixas[faixa]
    winsound.PlaySound(musica, winsound.SND_FILENAME)
    print('sound played') #ocultar 



import winsound


faixas = {
    'beep': 'button-32.wav',
    'badalada': 'badalada.wav'
}


def som(faixa):
    musica = faixas[faixa]
    winsound.PlaySound(musica, winsound.SND_FILENAME)
    print('sound played') #ocultar 



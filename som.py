import winsound


faixas = {
    'beep': 'som\\button-32.wav',
    'badalada': 'som\\badalada.wav',
    'carruagem_cidade': 'som\\carruagem_cidade.wav',
    'cozinha': 'som\\cozinha.wav',
    'dormindo': 'som\\dormindo.wav',
    'varrendo': 'som\\varrendo.wav',
}


def som(faixa):
    musica = faixas[faixa]
    winsound.PlaySound(musica, winsound.SND_FILENAME)
    #print('sound played') #ocultar (verificador)



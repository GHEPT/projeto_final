#Define a pontuação da personagem na etapa inicial no jogo.
class Score:
    def __init__(self):
        self.score = 0

    def pontuar(self, pontos):
        self.score += pontos
        print(f'Você pontuou. Seu SCORE agora é: {self.score}')

    
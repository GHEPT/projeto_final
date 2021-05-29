class Personagem:
    def __init__(self, score=0, stamina=100):
        self.stamina = 100
        self.score = 0
        self.nome = input('Digite o nome do personagem: ')

    def dormir(self):
        self.stamina = 100

        
    def pontuar(self, pontos):
        self.score += pontos
        print(f'Você pontuou. Seu SCORE agora é: {self.score}')

        



    


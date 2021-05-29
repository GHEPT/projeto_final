class Personagem:
    def __init__(self, score=0, stamina=100):
        self.stamina = 100
        self.score = 0
        self.nome = input('Digite o nome do personagem: ')

    def dormir(self):
        self.stamina = 100

        
    def pontuar(self, pontos):
        self.score += pontos
        #print(f'Você pontuou. Seu SCORE agora é: {self.score}') #Verificador

    def mudar_stamina(self, pontos):
        self.stamina += pontos

    def __str__(self):
        return f'{self.nome} tem {self.score} de pontuação e {self.stamina} de stamina.'

        



    


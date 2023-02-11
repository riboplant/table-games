import random

class Player:
    def __init__(self):
        self.puntos = 0
        self.D1 = dado
        self.D2 = dado
        self.D3 = dado
        self.D4 = dado
        self.D5 = dado

    def jugar(self,dados_disp):
        for x in range(dados_disp):




class dado:

    def tirar_dado(self):
        self.valor = random.randint(1, 7)

def mano(player):

    player.D1.tirar_dado()



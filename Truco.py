import random

Palos = { 1:"Espadas", 2:"Bastos", 3:"Oro", 4:"Copas" }
Valores_Truco = { (1,1): 14, (2,1): 13, (1,7):12, (3,7): 11, #Mas fuertes
                  (1,3): 10, (2,3): 10, (3,3): 10, (4,3): 10, #Los 3
                  (1,2): 9, (2,2): 9, (3,2): 9, (4,2): 9, (3,1): 8, (4,1): 8, #los 2 y anchos falsos
                  (1,12): 7, (2,12): 7, (3,12): 7, (4,12): 7,(1,11): 6, (2,11): 6, (3,11): 6, (4,11): 6, (1,10): 5, (2,10): 5, (3,10): 5, (4,10): 5, #figuras
                  (2,7): 4, (4,7): 4, (1,6): 3, (2,6): 3, (3,6): 3, (4,6): 3, (1,5): 2, (2,5): 2, (3,5): 2, (4,5): 2,(1,4): 1, (2,4): 1, (3,4): 1, (4,4): 1 } #Las debiles

class Jugador():
    def __init__(self, num_player, player_name):
        self.team = num_player % 2
        self.name = player_name
        if num_player == 1: self.Primero = True
        else: self.Primero = False
        self.mano = True

    def Assign_Cards(self):
        posibles_cartas = []
        mano_cartas_raw = []
        for i in range(1,41):posibles_cartas.append(i)
        for x in range(3):
            mano_cartas_raw.append(posibles_cartas[random.randint(1, len(posibles_cartas) - 1)])
            posibles_cartas.remove(mano_cartas_raw[x])

        self.Card1 = Carta(mano_cartas_raw[0])
        self.Card2 = Carta(mano_cartas_raw[1])
        self.Card3 = Carta(mano_cartas_raw[2])
        #print(self.Card1.palo, self.Card1.number_A)
        #print(self.Card2.palo, self.Card2.number_A)
        #print(self.Card3.palo, self.Card3.number_A)

    def Assign_embido(self):
        self.emb_temp_1 = self.Card1.Valor_embido
        self.emb_temp_2 = self.Card2.Valor_embido
        self.emb_temp_3 = self.Card3.Valor_embido
        self.mismo_palo = False

        if self.Card1.palo == self.Card2.palo == self.Card3.palo:
            self.mismo_palo = True

            if self.emb_temp_1 >= self.emb_temp_2 and self.emb_temp_2 >= self.emb_temp_3:
                self.Embido_1 = self.emb_temp_1
                self.Embido_2 = self.emb_temp_2

            elif self.emb_temp_1 >= self.emb_temp_3 and self.emb_temp_3 >= self.emb_temp_2:
                self.Embido_1 = self.emb_temp_1
                self.Embido_2 = self.emb_temp_3

            elif self.emb_temp_2 >= self.emb_temp_1 and self.emb_temp_1 >= self.emb_temp_3:
                self.Embido_1 = self.emb_temp_2
                self.Embido_2 = self.emb_temp_1

            elif self.emb_temp_2 >= self.emb_temp_3 and self.emb_temp_3 >= self.emb_temp_1:
                self.Embido_1 = self.emb_temp_2
                self.Embido_2 = self.emb_temp_3

            elif self.emb_temp_3 >= self.emb_temp_1 and self.emb_temp_1 >= self.emb_temp_2:
                self.Embido_1 = self.emb_temp_3
                self.Embido_2 = self.emb_temp_1

            elif self.emb_temp_3 >= self.emb_temp_2 and self.emb_temp_2 >= self.emb_temp_1:
                self.Embido_1 = self.emb_temp_3
                self.Embido_2 = self.emb_temp_2


        elif self.Card1.palo == self.Card2.palo:
            self.Embido_1 = self.emb_temp_1
            self.Embido_2 = self.emb_temp_2
            self.mismo_palo = True

        elif self.Card2.palo == self.Card3.palo:
            self.Embido_1 = self.emb_temp_2
            self.Embido_2 = self.emb_temp_3
            self.mismo_palo = True


        elif self.Card1.palo == self.Card3.palo:
            self.Embido_1 = self.emb_temp_1
            self.Embido_2 = self.emb_temp_3
            self.mismo_palo = True

        if self.mismo_palo == True: self.Valor_embido = 20 + self.Embido_1 + self.Embido_2
        else:
            if (self.emb_temp_1 >= self.emb_temp_2) and (self.emb_temp_1 >= self.emb_temp_3): self.Valor_embido = self.emb_temp_1
            if (self.emb_temp_2 >= self.emb_temp_1) and (self.emb_temp_2 >= self.emb_temp_3): self.Valor_embido = self.emb_temp_2
            if (self.emb_temp_3 >= self.emb_temp_1) and (self.emb_temp_3 >= self.emb_temp_2): self.Valor_embido = self.emb_temp_3

        #print(self.Valor_embido)

    def Movimiento(self):
        self.Action = input("1, 2, 3 cartas | 4 truco | 5, 6, 7 para los embidos (comun, real y falta): ")
        return self.Action

    def Show_CardsPlays(self):
        print(Palos.get(self.Card1.palo),self.Card1.number_A)
        print(Palos.get(self.Card2.palo),self.Card2.number_A)
        print(Palos.get(self.Card3.palo),self.Card3.number_A)
        print(str(self.Valor_embido) + " de embido")

class Carta():
    def __init__(self, card_id):
        self.id = card_id
        self.palo = int(self.id / 10) + 1
        self.number = self.id - ((self.palo - 1) * 10)
        if self.number >= 8: self.number_A = self.number + 2
        else: self.number_A = self.number  #Number_A es el numero de la carta, del 1 al 12 sin 8 y 9, el number va del 1 al 10 y es unicamente para asignar id

        if self.id%10 == 0: #caso id divisible por 10
            self.palo = (self.id / 10) - 1
            self.number_A = 10

        self.Valor_truco = Valores_Truco.get(self.palo,self.number_A)

        if self.number_A >= 10: self.Valor_embido = 0
        else: self.Valor_embido = self.number_A



def Mano(Player1, Player2, Mano):
    Player1.Show_CardsPlays()
    Movement = Player1.Movimiento()
    #Player 2 tambien

    for It in Jugador:

        if It.Primero == True: num_mano = 


#llamar a las funciones de truco, ronda comun, embido (aun no creadas)



#Cartas listas, falta crear el algoritmo del juego, las manos, los cantos, los puntos, el pie y mano, ciclar las manos
A = Jugador(1,1)
A.Assign_Cards()
A.Assign_embido()
B = Jugador(2,2)
B.Assign_Cards()
B.Assign_embido()


Mano(A,B,Mano)
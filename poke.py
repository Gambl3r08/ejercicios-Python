# Simulacion de juego pokemon
# Usare la libreria random para controlar los ataques, vida, def, vel. de los pokemon

import random


class Pokemon:
    # Se crea la vida, ataque, defe y vel
    def __init__(self, vida, atk, defe, vel):
        self.vida = vida
        self.atk = atk
        self.defe = defe
        self.vel = vel
        print("Se generon un pokemon")

    def generar(self):
        self.vida = random.randint(100, 125)
        self.atk = random.randint(30, 45)
        self.defe = random.randint(20, 25)
        self.vel = random.randint(70, 100)


poke1 = Pokemon
poke1.generar(poke1)
poke2 = Pokemon
poke2.generar(poke2)

if poke1.vel < poke2.vel:
    poke1.vida - poke2.atk
    print("la vida restante del pokemon 1 es: ", poke1.vida)

else:
    poke2.vida - poke1.atk
    print("La vida restante del pokemon 2 es: ", poke2.vida)
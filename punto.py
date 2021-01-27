from validaciones import *
class Punto():
    # Representar un punto en un plano
    def __init__(self, x=0, y=0):
        if es_numero(x) and es_numero(y):
            self.x = x
            self.y = y
        else:
            raise TypeError("X e Y Deben ser valores numericos ")

    def distancia(self, otro):
        r = self.restar(otro)
        return (dx*dx + dy*dy)**0.5


    def restar(self, otro):
        return Punto(self.x - otro.x, self.y - otro.y)


    def norma(self):
        return(self.x*self.x + self.y*self.y)**0.5

    def __str__(self):
        return ("(", str(self.x), ", ", str(self.y), ")")

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Punto(self.x - otro.x, self.y -otro.y)
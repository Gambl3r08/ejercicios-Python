class bici():

    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color
        print("Tipo establecido")
        print("Color establecido")

    def andar(self, n):
        self.n = n
        print("la bici ando: ", n, " metros")


x = bici("bmx", "rojo")
x.andar(10)
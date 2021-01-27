#clases


class Antena():
    color = ""
    longitud = ""

class Pelo():
    color = ""
    textura = ""

class Ojo():
    forma = ""
    color = ""
    tamanio = ""

class Objeto():
    color = ""
    tamanio = ""
    aspecto = ""
    antenas = Antena()  #Propiedade compuesta por el objeto Antena()
    ojos = Ojo()  #Propiedad compuesta por el objeto Ojos()
    pelos = Pelo()  #Propiedad compuesta por el objeto Pelo()

    def flotar(self):
        print("estoy flotando")


et = Objeto()
print (et.color)
print (et.tamanio)
print (et.aspecto)
et.color = "rosa"
print (et.color)



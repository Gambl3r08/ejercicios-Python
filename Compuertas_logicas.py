class CompuertaLogica:
    
    def __init__(self, n):
        self.etiqueta = n
        self.salida = None

    def obtenerEtiqueta(self):
        return self.etiqueta


    def obtenerSalida(self):
        self.salida = self.ejecutarLogicaDeCompuerta()
        return self.salida

class CompuertaBinaria(CompuertaLogica):
    
    def __init__(self, n):
        compuertaLogica.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def obtenerPinA(self):
        return int(input("Ingrese la entrada del Pin A para la compuerta: "+ self.obtenerEtiqueta()+ "--->"))


class CompuertaUnaria(CompuertaLogica):
    
    def __init__(self, n):
        CompuertaLogica.__init__(self, n)

        self.pin = None

    def ObtenerPin(self):
        return int(input("Ingrese la entrada del Pin para la compuerta: "+ self.obtenerEtiqueta()+ "--->"))
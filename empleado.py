class Empleado:
    def __init__(self):
        self.nombre = input("ingrese el nombre ")
        self.sueldo = input("Ingrese el sueldo ")


    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Sueldo: ", self.sueldo)

    def paga_impuesto(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos.")
        else:
            print("No paga impuestos")



# Main

empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_impuesto()
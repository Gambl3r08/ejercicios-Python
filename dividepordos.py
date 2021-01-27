from pila import *

def dividirPor2(numeroDecimal):
    pilaResiduo = Pila()
    
    
    while numeroDecimal > 0:
        residuo = numeroDecimal % 2
        pilaResiduo.incluir(residuo)
        numeroDecimal = numeroDecimal // 2
        
    cadenaBinaria = ""
    
    while not pilaResiduo.estaVacia():
        cadenaBinaria = cadenaBinaria + str(pilaResiduo.extraer())
        
        
    return cadenaBinaria
    

def convertirBase(numeroDecimal, base):
    digitos = "0123456789ABCDEF"
    
    pilaResiduo = Pila()
    
    while numeroDecimal > 0:
        residuo = numeroDecimal % base
        pilaResiduo.incluir(residuo)
        numeroDecimal = numeroDecimal // base
        
    nuevaCadena = ""
    
    while not pilaResiduo.estaVacia():
        nuevaCadena = nuevaCadena + digitos[pilaResiduo.extraer()]
        
    return nuevaCadena


print(convertirBase(26, 26))
print(dividirPor2(10))
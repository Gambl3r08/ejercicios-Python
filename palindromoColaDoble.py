from colaDoble import *

def verificarPalindromo(cadena):
    
    colaDobleCaracteres = ColaDoble()
    for caracter in cadena:
        colaDobleCaracteres.agregarFinal(caracter)
        
    aunIguales = True
    
    while colaDobleCaracteres.tamano() > 1 and aunIguales:
        primero = colaDobleCaracteres.removerFrente()
        ultimo = colaDobleCaracteres.removerFinal()
        if primero != ultimo:
            aunIguales = False
            
    return aunIguales
    
if verificarPalindromo("radar") == True:
    print("Es palindromo")
else:
    print("No es palindromo")
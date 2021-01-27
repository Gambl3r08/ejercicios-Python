from cola import *

def papaCaliente(listaNombres, N):
    colaSimulacion = Cola()
    for nombre in listaNombres:
        colaSimulacion.agregar(nombre)
        
    while colaSimulacion.tamano() > 1:
        for i in range(N):
            colaSimulacion.agregar(colaSimulacion.avanzar())
        
        colaSimulacion.avanzar()
        
    return colaSimulacion.avanzar()
    
print(papaCaliente(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
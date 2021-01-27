# Mediremos el tiempo de ejecución de un programa utilizando la libreria: time
import time

def sumaDeN2(n):
    inicio = time.time()

    laSuma = 0
    for i in range(1, n+1):
        laSuma = laSuma + i

    final = time.time()

    return laSuma, final-inicio
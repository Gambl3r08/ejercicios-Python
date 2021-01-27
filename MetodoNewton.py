def raizCuadrada(n):
    """
    estima la raiz cuadrada en 20 intervalos
    """

    raiz = n/2 # La estimacion inicial sera 1/2 de n
    for k in range(20):
        raiz = (1/2)*(raiz + (n / raiz))

    return raiz
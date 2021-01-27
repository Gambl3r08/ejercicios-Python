def sumaLista(listaNumeros):
    if len(listaNumeros) == 1:
        return listaNumeros[0]
    else:
        return listaNumeros[0] + sumaLista(listaNumeros[1:])

print(sumaLista([1, 2, 3, 4, 5, 6, 7, 8, 9]))
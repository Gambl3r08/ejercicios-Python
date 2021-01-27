def contarElementos(lista):
    return {i:lista.count(i) for i in lista}


lista = [1, 2, 1, 1, 3, 2, 4]

resul = contarElementos(lista)
maximo=max(resul, key=resul.get)

print("valor mas repetido: ",maximo," :: ",resul[maximo]," veces")
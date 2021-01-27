def anagrama(cadena1, cadena2):
    unaLista = list(cadena2)

    pos1 = 0
    aunOK = True

    while pos1 < len(cadena1) and aunOK:
        pos2 = 0
        encontrado = False
        while pos2 < len(unaLista) and not encontrado:
            if cadena1[pos1] == unaLista[pos2]:
                encontrado = True
            else:
                pos2 = pos2 + 1

        if encontrado:
            unaLista[pos2] = None
        else:
            aunOK = False

        pos1 = pos1 + 1

    return aunOK


def comparar(cadena1, cadena2):
    unaLista1 = list(cadena1)
    unaLista2 = list(cadena2)

    unaLista1.sort()
    unaLista2.sort()

    pos = 0
    coincide = True

    while pos < len(cadena1) and coincide:
        if unaLista1[pos] == unaLista2[pos]:
            pos = pos + 1
        else:
            coincide = False

    return coincide


def contar(cadena1, cadena2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(cadena1)):
        pos = ord(cadena1[i]) - ord('a')
        c1[pos] = c1[pos] + 1


    for i in range(len(cadena2)):
        pos = ord(cadena2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    aunOK = True
    while j < 26 and aunOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            aunOK = False

    return aunOK

print(contar('cero', 'ocre'))
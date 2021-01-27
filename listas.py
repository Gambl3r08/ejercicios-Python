# Agregar elementos al final de la lista
nombres_masculinos = ["Roberto", "Alvaro", "Miguel"]
nombres_masculinos.append("Jose")

print  (nombres_masculinos)


# Agregar varios elementos al final de la lista

nombres_masculinos.extend(["Andres", "Enrrique"])
print(nombres_masculinos)

# Agregar un elemento en una posición determinada

nombres_masculinos.insert(0, "Primera posicion")

print(nombres_masculinos)

# Eliminar el ultimo elemento de la lista

nombres_masculinos.pop()

print(nombres_masculinos)

# Eliminar un elemento por su indice

nombres_masculinos.pop(3)

print(nombres_masculinos)

# Eliminar un elemento por su valor

nombres_masculinos.remove("Roberto")

print(nombres_masculinos)

# Ordenar una lista en reversa

nombres_masculinos.reverse()

print(nombres_masculinos)

# Ordenar una lista en forma ascendente

nombres_masculinos.sort()

print(nombres_masculinos)

# Ordenar una lista en forma descendente

nombres_masculinos.sort(reverse=True)

print(nombres_masculinos)

# Contar cantidad de apariciones de elementos

print(nombres_masculinos.count("Jose"))

# Obtener numero de indice

print(nombres_masculinos.index("Alvaro"))

# Conversion de tipos

tupla = (1, 2, 3, 4, 5)
list(tupla)
lista = [1, 2, 3, 4]
tuple(lista)


# Concatenacion simple de colecciones

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6, 7, 8]
lista3 = lista1 + lista2
print(lista3)

tupla1 = (1, 2, 3, 4, 5)
tupla2 = (4, 6, 8, 10)
tupla3 = (3, 5, 7, 9)
tupla4 = tupla1 + tupla2 + tupla3

print(tupla4)

# Valor maximo y minimo

print (max(tupla4))

print(min(tupla4))

print (max(lista3))
print (min(lista3))


#Contar elementos

print(len(lista3))

print(len(tupla4))


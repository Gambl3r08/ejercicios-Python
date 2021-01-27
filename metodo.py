# Metodos de eliminacion

# Vaciar un deccionario

diccionario = {"color" : "violeta", "talle" : "XS", "Precio": 174.25}

print(diccionario)

diccionario.clear()
print(diccionario)

# Copiar un diccionario
diccionario = {"color" : "violeta", "talle" : "XS", "Precio": 174.25}
copia = diccionario.copy()

print(copia)

# Crear un nuevo diccionario desde las claves de una secuencia

secuencia = ["color", "talle", "marca"]

diccionario1 = dict.fromkeys(secuencia)

print(diccionario1)

diccionario2 = dict.fromkeys(secuencia, 'valor x defector')
print(diccionario2)

# Concatenar diccionarios

diccionario1.update(diccionario2)

print(diccionario1)


# Establecer una clave y valor por defecto

remera = {"color": "rosa", "marca": "Zara"}

clave = remera.setdefault("talle", "U")

print(clave)

print(remera)

# Obtener el valor de una clave

print(remera.get("color"))


# Saber si una clave existe en el diccionario

existe = "color"

print(existe in remera)


# Obtener las claves y valores de un diccionario

for clave, valor in diccionario.items():
    print("El valor de la clave es %s es %", clave, valor)

# Obetener claves de un diccionario

print(diccionario1.keys)


# Obtener los valores de un diccionario

valores = diccionario.values()

print(valores)

# Obtener la cantidad de elementos de un diccionario

print(len(diccionario))
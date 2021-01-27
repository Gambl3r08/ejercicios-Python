import random

# Generar numeros aleatorios entre 49999 y 99999
lista = []

for n in range(0, 50):
    lista.append(random.randint(49999, 99999))

# Elegir numero al azar

numero_al_azar = random.choice(lista)
print (numero_al_azar)

# Elegir 5 numeros al azar

numero_al_azar = random.sample(lista, 5)

print (numero_al_azar)

semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

print (random.shuffle(semana))
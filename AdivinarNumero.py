# modulo para numeros aleatorios
import random
# conjunto de digitos
digitos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

# codigo
codigo = ''


for i in range(4):
    candidato = random.choice(digitos)
    # candidato = int(candidato)
    # Elegimos digitos
    while candidato in codigo:
        candidato = random.choice(digitos)
    codigo = codigo + candidato

# iniciamos iteracion del usuario
print("Bienvenido")
print("Tienes que adivinar un numero de 4 cifras distintas")
propuesta = input("¿Que codigo propones? ")


intentos = 1

while propuesta != codigo:
    intentos = intentos + 1
    aciertos = 0
    coincidencias = 0

    # Verificamos el codigo
    for i in range(4):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    print("Tu propuesta (", propuesta, ") tiene ", aciertos, "aciertos y ", coincidencias, "coincidencias")

    propuesta = input("Propon otro codigo ")
print("Te tomo: ", intentos, " intentos")
print("felicidades, adivinaste el codigo, ganaste!")
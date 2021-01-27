from random import *


lista = []
for i in range(10):
    lista.append(randint(1, 100))

for i in range(10):
    print(lista[i])
    
print("el valor maximo en la lista es: ",max(lista))
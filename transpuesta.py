transpuesta = []
matriz = [
         [1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
]
for i in range(4):
    fila_transpuesta = []
    for fila in matriz:
        fila_transpuesta.append(fila[i])
    transpuesta.append(fila_transpuesta)
print(transpuesta)
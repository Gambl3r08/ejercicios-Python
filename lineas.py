
Lista1 = []

# Dentro del metodo que lee las lineas 

cont = 0

if cont == 0:
	Lista1.append(linea)
	cont = 1

Lista2 = []
if linea.isalpha():
	Lista1.append(linea)
	if Lista1[-1].isalpha():
		Lista1.insert(-2,Lista2)
		Lista2 = []

if linea.isnumeric():
    Lista2.append(linea)





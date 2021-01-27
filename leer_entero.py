def lee_entero():
    intentos = 0
    while intentos < 5:
        valor = input("ingrese un numero entero ")
        try:
	    valor = int(valor)
	    return valor
	except ValueError:
	    intentos += 1
    raise ValueError, "Valor incorrecto ingresado en 5 intentos"
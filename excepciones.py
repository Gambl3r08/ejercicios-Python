while True:
    try:
        x = int(input("Ingrese un numero: "))
        break
    except ValueError:
        print("No es valido")
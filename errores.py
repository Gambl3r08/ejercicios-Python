def suma(a, b):
    int(a)
    int(b)
    return a + b

while True:
    try:
        x = int(input("ingrese un numero A: "))
        y = int(input("ingrese un numero B: "))
        break
    except ValueError:
        print("No fue valido, ingrese de nuevo.")

print(suma(x, y))
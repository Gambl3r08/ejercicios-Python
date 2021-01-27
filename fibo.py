#Modulo de numeros Fibonacci

def fib(n): #Escribir la serie Fibonacci hasta n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
def fib2(n): #Devolver serie Fibonacci hasta n
    resultado = []
    a , b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado
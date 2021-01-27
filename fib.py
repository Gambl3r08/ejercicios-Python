# Serie fibonacci con while
# Por parametro un N entero con el rango
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
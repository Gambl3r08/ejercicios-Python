def divisors(integer):
    int(integer)
    lista = []
    n = 1
    while n <= integer:
        if integer / n % 2 == 0:
            lista.append(n)
        n += 1
    print(lista)


divisors(12)

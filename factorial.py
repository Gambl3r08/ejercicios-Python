def factorial(n):
    assert n >= 0, "n debe ser mayor igual a 0"
    fact = 1
    for i in xrange(2, n + 1):
        fact *= i
    return fact
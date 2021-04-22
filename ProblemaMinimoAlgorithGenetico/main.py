import random

min, max = -5.0, 5.0

def generarRand(min, max):
    randNum = random.randint(min, max)
    return randNum


def resolver(x, y):
    mi = 5
    listaPadres = []

    for _ in range(mi):
        listaPadres.append(generarRand(min, max))
    
    

    func = (x**4) + (y**4) - (1.8*(x**3)) - (1.5*(y**3))-(2*(y**2))+(3*x)+(3*y)
    
    return func


print(resolver(3, 2))
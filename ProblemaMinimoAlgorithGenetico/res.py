from array import array
from matplotlib.pyplot import fill
from statistics import *
from random import *
from itertools import *

def function(x, y):
    return x**4 + y**4 + x**4 - x**2 +(2*(y**2)) - (3*(x**2)) + (2(x**2)) -y -x


def fill():
    for _ in range(5):
        array[0].append(random.uniform(-5, 5))
        array[1].append(random.uniform(-5, 5))

miu =5
parents = fill()


firstSigma = True
change = True



for time in range(5000):
    recombinations = ['discrete', 'global', 'local']
    children = [[], []]
    competition = {}


    if firstSigma:
        sigma = stdev(list(chain(*parents)))
        firstSigma = False
    
    else:
        sigma = sigma * 2.718**(0.7072)* random.uniform(-0.99, 0.99)
        if sigma <= 0.15:
            sigma = 0.15
    
    for i in range(28):
        position = random.randint(0, 4)
        children[0].append(parents[0][position]+(random.uniform(-0.99, 0.99)*sigma))
        children[1].append(parents[1][position]+(random.uniform(-0.99, 0.99)*sigma))
    
    for j in range(7):
        choice = random.choice(recombinations)
        if choice == 'discrete':
            children[0].append(parents[0][random.randint(0, 4)])
            children[1].append(parents[1][random.randint(0, 4)])
        
        elif choice == 'global':
            recombinations.remove('global')
            children[0].append(1 / sum(parents[0]))
            children[1].append(1 / sum(parents[0]))

        elif choice == 'local':
            position_1 = random.randint(0, 4)
            position_2 = random.randint(0, 4)
            while position_1 == position_2:
                position_2 = random.randint(0, 4)

            number = random.uniform(0, 1)
            children[0].append(
                (number * parents[0][position_1]) + ((1 - number) * parents[0][position_2])
            )
            children[1].append(
                (number * parents[1][position_1]) + ((1 - number) * parents[1][position_2])
            )

    for index in range(5):
        competition.update({function(parents[0][index], parents[1][index]): index})
    
    for index in range(35):
        competition.update({function(children[0][index], children[1][index]): index + 5})
    
    results = list(dict(sorted(competition.items(), key=itemgetter(0))).values())

    for i in range(5):
        if results[i] <= 4:
            parents[0][i] = parents[0][results[i]]
            parents[1][i] = parents[1][results[i]]
        else:
            parents[0][i] = children[0][results[i]-5]
            parents[1][i] = children[1][results[i]-5]




    print("==================================================")
    print("X =", parents[0][0])
    print("Y =", parents[1][0])
    print("Minimun = ", function(parents[0][0], parents[1][0]))
    print("==================================================")
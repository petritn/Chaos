"""This is an example of the Chaos Theory - Lorenz's investigation
into the Malthusian population growth model."""

import numpy as np
import pylab as pl

def chaos(p, r, g):
    n = 0
    result = []
    generation = []
    while n < g:
        result.append(p)
        p_next = r * p * (1 - p)
        generation.append(n)
        print(p)
        p = p_next
        n = n + 1
    return generation, result

def inputR():
    print('Please specify the initial population size?')
    pop = float(input())
    print('Please specify the rate of growth?')
    rog = float(input())
    print('Please specify the number of generations?')
    gen = int(input())
    return pop, rog, gen

p, r, g = inputR()
x, y = chaos(p, r, g)

pl.plot(x, y)
pl.title('Modified Malthusian Population Growth Model - CHAOS')
pl.xlabel('Number of Generations')
pl.ylabel('Population Size')
pl.ylim(0.0, 1.0)
pl.grid()
pl.show()

#End of file - just validating github

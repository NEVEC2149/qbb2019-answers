#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math

def simulation(p, f, t):
    counter = []
    for i in range(t):
        freq = f
        gen = 0
        while True:
            prob = np.random.binomial(2 * p, freq)
            freq = prob/( 2 * p ) 
            gen += 1
            if (freq == 0.0) or (freq == 1.0):
                break
        counter.append(gen)
    return(counter)

freq = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

values = {}
for f in freq:
    r = simulation(100, f, 100)
    values[f] = r

for p in freq:
    for v in values[p]:
        plt.scatter(x=p, y=v, alpha= 0.8)
    plt.savefig("freq_vs_time.png")
#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math

def simulation(p, f, t, sc):
    for i in range(t):
        freq = f
        gen = 0
        while True:
            prob = np.random.binomial(2 * p, freq)
            freq = (prob*(1+sc)) / ((2 * p) - prob + (prob * (1+sc)))
            gen += 1
            if (freq == 0.0) or (freq == 1.0):
                break
    return(gen)

s_coeff = [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

fr = []

for n in s_coeff: 
    f = simulation(1000, 0.5, 10, n)
    fr.append(f)
    
# print(fr)

fig, ax = plt.subplots()
plt.scatter(x = s_coeff, y = fr, alpha = 0.5, color = "green")
fig.savefig("selection coefficient.png")
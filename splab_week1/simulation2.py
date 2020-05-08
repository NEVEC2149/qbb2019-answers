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
    return(gen)
    
population = [100, 1000, 10000, 100000, 1000000, 10000000]
gen = []
size = []

for n in population:
    fix = simulation(n, 0.5, 1)
    gen.append(math.log10(fix))
    size.append(math.log10(n))

fig, ax = plt.subplots()
ax.plot(size, gen, color = "blue")
ax.set_title("Log Population vs. Fixation Time")
ax.set_xlabel("Log population size")
ax.set_ylabel("Log generations")
fig.savefig("p_size_vs_time.png")
plt.close(fig)
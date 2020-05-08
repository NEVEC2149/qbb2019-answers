#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

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

    fig, ax = plt.subplots()
    hist = ax.hist(counter)
    ax.set_title("1000 Time-to-fixation Simulations")
    ax.set_xlabel("Generation")
    ax.set_ylabel("Trials")                      
    fig.savefig("1000_trials.png")       
    plt.close(fig)
    
simulation(100, 0.5, 1000)
#!/usr/bin/env python3

import numpy as np
import pandas as pd

s = "CATAAACCCTGGCGCGCTCGCGGCCCGGCACTCTTCTGGTCCCCACAGACTCAGAGAGAACCCACCATGGTGCTGTCTCCTGCCGACAAG"\
        "ACCAACGTCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGATGTTCCTGTCCTTCCCCA"\
        "CCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAAGGTGGCCGACGCGCTGACCAA"\
        "CGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGCGACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTC"\
        "AAGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCC"\
        "TGGCTTCTGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTTCTTGCCCCTTGGGCCTCCCCCCAGCC"\
        "CCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCAAAAAAAAAAAAAAAAAAAAAA"

t = "GGGGCTGCCAACACAGAGGTGCAACCATGGTGCTGTCCGCTGCTGACAAGAACAACGTCAAGGGCATCTTCACCAAAATCGCCGGCCATGC"\
        "TGAGGAGTATGGCGCCGAGACCCTGGAAAGGATGTTCACCACCTACCCCCCAACCAAGACCTACTTCCCCCACTTCGATCTGTCACACGGCT"\
        "CCGCTCAGATCAAGGGGCACGGCAAGAAGGTAGTGGCTGCCTTGATCGAGGCTGCCAACCACATTGATGACATCGCCGGCACCCTCTCCAAG"\
        "CTCAGCGACCTCCATGCCCACAAGCTCCGCGTGGACCCTGTCAACTTCAAACTCCTGGGCCAATGCTTCCTGGTGGTGGTGGCCATCCACCA"\
        "CCCTGCTGCCCTGACCCCGGAGGTCCATGCTTCCCTGGACAAGTTCTTGTGCGCCGTGGGCACTGTGCTGACCGCCAAGTACCGTTAAGACG"\
        "GCACGGTGGCTAGAGCTGGGGCCAACCCATCGCCAGCCCTCCGACAGCGAGCAGCCAAATGAGATGAAATAAAATCTGTTGCATTTGTGCTCCAG"

sigma = [[91, -114, -31, -123],[-114, 100, -125, -31],[-31, -125, 100, -114],[-123, -31, -114, 91]]
sigma = pd.DataFrame(sigma)
sigma.columns = ["A","C","G","T"]
sigma.index = ["A","C","G","T"]
gap = 300
delta = gap


# Initialize the matrix
F = np.zeros((len(s)+1,len(t)+1), dtype=int)
trace = np.zeros((len(s),len(t)), dtype=str)
for i in range(1, F.shape[0]):
    F[i][0] = F[i-1][0] - delta
    
for j in range(1, F.shape[1]):
    F[0][j] = F[0][j-1] - delta
    

# Fill in each cell of the matrix according to maximization
for i in range(1, F.shape[0]):
    for j in range(1, F.shape[1]):
        v = F[i-1][j] - delta
        h = F[i][j-1] - delta
        d = F[i-1][j-1] + sigma.at[s[i-1],t[j-1]]
        value_list = [v,h,d]
        
        F[i][j] = max(value_list)
        # Diagonal prior to vertical and horizontal
        if max(value_list) == d:
            trace[i-1][j-1] = "d"
        elif max(value_list) == v:
            trace[i-1][j-1] = "v"
        else:
            trace[i-1][j-1] = "h"
            
            
# Traceback
i,j = F.shape[0]-1, F.shape[1]-1
s_aligned = ""
t_aligned = ""
score = F[i,j]
while i > 0 and j > 0:
    if trace[i-1][j-1] == "v":
        s_aligned = s[i-1] + s_aligned
        t_aligned = "-" + t_aligned
        i -= 1
    elif trace[i-1][j-1] == "h":
        s_aligned = "-" + s_aligned
        t_aligned = t[j-1] + t_aligned
        j -= 1
    else:
        s_aligned = s[i-1] + s_aligned
        t_aligned = t[j-1] + t_aligned
        i -= 1
        j -= 1
        

with open("Output.txt", "w") as text_file:
    text_file.write("sequence 1: \n")
    text_file.write(s_aligned + "\n\n")
    text_file.write("sequence 2: \n")
    text_file.write(t_aligned + "\n\n")
    text_file.write("Score: \n")
    text_file.write(str(score))
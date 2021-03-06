#!/usr/bin/env python3

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
#Specify transctipt of interest
t_name = sys.argv[1]
#Load Metadata
samples = pd.read_csv(sys.argv[2])
ctab_dir = sys.argv[5]
#Load Metadata
def sex_sorter(sex):
   soi = samples.loc[:,"sex"] == sex
   stages = samples.loc[soi, "stage"]
   #print(srr_ids)
   #Load FPKMS
   fpkms = pd.read_csv(sys.argv[3], index_col="t_name")
   #Extract Data
   my_data = []
   for stage in stages:
       #print(srr_id)
       my_data.append(fpkms.loc[t_name,sex+ '_' +stage])
   return my_data
def sex_replicate(sex):
   samples = pd.read_csv(sys.argv[4])
   soi = samples.loc[:,"sex"] == sex
   srr_ids = samples.loc[soi, "sample"]
   my_data = []
   for srr_id in srr_ids:
       # my_data(my_data.loc[t_name, srr_id])
       #print(srr_id)
       #my_data.append(fpkms.loc[t_name,srr_id])
       ctab_path = os.path.join(ctab_dir, srr_id,
                               "t_data.ctab")
       #print(ctab_path)
       df = pd.read_csv(ctab_path, sep="\t",
                       index_col="t_name")
       # my_data["gene_name"] = df.loc[:,"gene_name"]
       my_data.append(df.loc[t_name, "FPKM"])
   return my_data
#Print my_data
#print(my_data)
male_data = sex_sorter("male")
male_data_rep = sex_replicate("male")
female_data = sex_sorter("female")
female_data_rep = sex_replicate("female")
labelz = ["male", "female"]
labelz2 = ["10", "11", "12", "13", "14", "14A", "14B", "14C", "14D"]
#Plot
fig, ax = plt.subplots()
plt.title("Male and Female Data for Sxl Transcripts")
plt.xlabel("Embryonic Stage")
plt.ylabel("mRNA Abundance")
ax.plot(male_data, color="blue")
ax.plot(female_data, color="red")
ax.plot(range(4,8), male_data_rep, 'o', color="blue")
ax.plot(range(4,8), female_data_rep, 'o', color="red")
plt.legend(labels= labelz, loc= "center left", bbox_to_anchor=(1, 0.5))
plt.tight_layout()
ax.set_xticklabels(labelz2, rotation='vertical')
ax.set_xticks(np.arange(len(labelz2)))
fig.savefig("timecourse_male_female.png")
plt.close(fig)

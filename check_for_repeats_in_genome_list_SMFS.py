import os
import pandas as pd
import subprocess

df = pd.read_csv('Euk5_genome_download_edit.csv', sep = ',')
genome_name= list(df['genome_name'])
index =df.set_index('genome_name', inplace=True)
Genome= './databases/Eukarya5/genomes/'
abbreviation_pair = df.loc[genome_name]['Abbreviation']
#if you wish to count the number of overlaps use count = count+1
count = 0
for i in genome_name:
    for genome in os.listdir(Genome):
        if i == genome in os.listdir(Genome):
#to run the entire process
       #     subprocess.run(['echo',databases/Eukarya5/genomes/genome, abbreviation_pair[i]])

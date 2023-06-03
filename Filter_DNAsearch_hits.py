import os
from Bio import SeqIO
import pandas as pd
#Get list of record.ids and start/end point of the sequence
#little clean up as the columns 5,6 have the 25kb added/substracted (accounted for start<25000 as well and set at 0), to account for possible shifts, introns or large genes


df = pd.read_csv("./Agust_list.tsv", sep = '\t', header = None)
df = df.drop([0])
df = df.drop(columns=[1,2,4])
df.rename(columns={0:'DNA_id', 5: 'start', 6: 'end', 3: 'evalue'}, inplace=True)
df['start'] = df['start'].astype(int)
df['end'] = df['end'].astype(int)

#set index so that both the start and end are taken for the right DNA_id
#then print each out to check if each sequence has the right start and end attached before searching with SeqIO

DNA_id= list(df['DNA_id'])
index =df.set_index('DNA_id', inplace=True)

#with count +=1 i have made sure that the amount of i ==record.id matches line up when looping through df['DNA_id'], it is at
43, so the matching works

with open("/home/mick/TBB_internship/databases/Eukarya5/genomes/abbreviation/done/correct/Euk5_genomes_concact.fa") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        for i in df[index]:
            if i  == record.id:
                 start = df[index,'start']
                 end = df[index,'end']
                 new = ("{}_{}_{}.fa").format(i,start,end)
                 print(new)
              
hits_ids  = df['subject acc.ver'].tolist()
hits_ids = [x.split('_')[1] for x in hits_ids]
new_hits = [x for x in hits_ids if x[0:6] not in ortho_ids]
#print(new_hits)

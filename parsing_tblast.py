import os
import pandas as pd
import subprocess
df = pd.read_csv('Euk5_genome_download_edit.csv', sep = ',')
df = pd.read_csv('./M18BP1vEUK5_p_TBLASTN', sep = '\t', header = None)
df.columns = ['query acc.ver','subject acc.ver','% identity','alignment length','mismatches','gap opens','q. start','q. end','s. start','s. end','evalue','bit score']
df_edit = df[['query acc.ver','subject acc.ver','s. start', 's. end','evalue']]
df_edit["Query_id"] = (df_edit['query acc.ver'].str.split('0',expand = True,)[0])


protein_name= list(df_edit["Query_id"])
index =df.set_index('Suject_id', inplace=True)
Genome= './'
abbreviation_pair = df.loc[genome_name]['Abbreviation']
#if you wish to count the number of overlaps use count = count+1
count = 0
for i in genome_name:
    for query_id in os.listdir(Genome):
        if i == genome in os.listdir(Genome):
import pandas as pd
#if query is not in directionairy append

df = pd.read_csv('./M18BP1vEUK5_p_TBLASTN', sep = '\t', header = None)
df.columns = ['query acc.ver','subject acc.ver','% identity','alignment length','mismatches','gap opens','q. start','q. end','s. start','s. end','evalue','bit score']
df_edit = df[['query acc.ver','subject acc.ver','s. start', 's. end','evalue']]

df_edit["Subject_id"] = (df_edit['subject acc.ver'].str.split('0',expand = True,)[0].str.split('_', expand= True,)[1])
df_edit["Query_id"] = (df_edit['query acc.ver'].str.split('0',expand = True,)[0])
index =df_edit.set_index('Subject_id', inplace=True)
#df_edit.loc[~(df_edit["Subject_id"] == df_edit["Query_id"])]
list_1 =df_edit.values.tolist("Subject_id", "Query_id")ZZ
#df_edit.iloc[df_edit["Subject_id"] == df_edit["Query_id"]]
#for i in df_edit:
#    if df_edit["Query_id"] != i:
#     df_left.append(index)
print(list_1)

#df.columns["Database"] = df
#df.columns["Query"]columns = [columns = [columns = [columns = [columns = [


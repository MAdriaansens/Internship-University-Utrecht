import pandas as pd 
#Euk5_hitsvPI = pd.read_csv('.//ids/M18BP1_fl_ids.csv', comment = '#', header = None, delim_whitespace = True)
hitsvPI = pd.read_csv('./M18BP1/ids/M18BP1_orthologs_euk5_ids.csv', comment = '#', header = None, delim_whitespace = True)

hitsvPI.columns = ['protein_ID']

hitsvPI['Abbrev'] = hitsvPI['protein_ID'].str[0:6]
uniques = pd.DataFrame()
uniques['Abbrev'] = (hitsvPI['Abbrev'].unique())
uniques['hits'] = '1'
print(uniques)


Species_ID = pd.read_csv('./databases/Chordata/Chordata_ids.csv', header = None, comment = '#', sep = '\t')
Species_ID = Species_ID.iloc[:,::-1]
#Species_ID.columns = ['Abbrev']
Species_ID.columns = ['Newick_name', 'Abbrev']
print(Species_ID)
#merged_df = (Species_ID.set_index('Abbrev').combine_first(uniques.set_index('Abbrev')).reset_index())
merged_df = uniques.merge(Species_ID, how = 'outer')
#merged_df = pd.merge(uniques, Species_ID, on=['Abbrev','hits'])
print(merged_df)

merged_df['hits'] = merged_df['hits'].fillna(0)
hits_species = merged_df[['Newick_name', 'hits']]
hits_species.to_csv(r'/home/mick/TBB_internship/M18BP1_hit_euk5.txt', header=None, index=None, sep=',', mode='a')

print(hits_species)

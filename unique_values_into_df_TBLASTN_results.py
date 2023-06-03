import pandas as pd

#first put all the correct headers on the dataframe for later
df = pd.read_csv('./M18BP1vEUK5_p_TBLASTN', sep = '\t', header = None)
df.columns = ['query acc.ver','subject acc.ver','% identity','alignment length','mismatches','gap opens','q. start','q. end','s. start','s. end','evalue','bit score']
df_edit = df[['query acc.ver','subject acc.ver','s. start', 's. end','evalue']]

df_edit["Subject_id"] = (df_edit['subject acc.ver'].str.split('0',expand = True,)[0].)
df_edit["Query_id"] = (df_edit['query acc.ver'].str.split('0',expand = True,)[0])
df_unique_values =[]

#first loop through the df to see if some ids equal the Subject and then remove these.
 
for i in df_edit:
    if (df_edit.iloc[df_edit["Subject_id"] == df_edit["Query_id"]]) == FALSE:
    df_unique_values.append(i)
print(df_unique_values)

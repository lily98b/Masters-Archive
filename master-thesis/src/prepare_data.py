import os
from collections import defaultdict


"""
Doing multilabel prediction task with go_label data of level 4th, the number of label counts is from 1k to 10k, the rest, having
less counts, are not considered in this dataset. 
"""

#loading the level4, go data and extract thse labels having between 1k t 10k counts.
os.chdir("/PATH/to/go_label")
with open("go_level4_label.txt") as f:
  go_data = f.read()
  
go_data = [i.split("\n") for i in go_data.split("\t")][1:] #as the data is in tab format, turning it int a list of labels 
for i in go_data:
  i[1] = i[1].split("_")[0]
  

go_data_dict=defaultdict(list)
for i in go_data:
  go_data_dict[i[1]].append(i[0])
  
data_unique = {key: sorted(set(value)) for key, value in go_data_dict.items()}
sorted_data = dict(sorted(data_unique.items(), key= lambda x: len(x[1]), reverse=True))

#counting the labels and extracting the ones havong more than 1k counts
labels = []
labels.extend(x for j in sorted_data.values() for x in j)

go_labels = {'GO:0043169': 10203,
         'GO:0043168': 6863,
         'GO:0000166': 6642,
         'GO:0032555': 5040,
         'GO:0035639': 4847,
         'GO:0003677': 3371,
         'GO:0003723': 3040,
         'GO:0016773': 2552,
         'GO:0016301': 2198,
         'GO:0016818': 1999,
         'GO:0019900': 1536,
         'GO:0004553': 1453,
         'GO:0004175': 1387,
         'GO:0004518': 1237,
         'GO:0042803': 1200,
         'GO:0001067': 1088,
         'GO:0020037': 1008}

filtered_ontologies ={}
for i,j in sorted_data.items():
  j =[k for k in j if k in go_labels]
  filtered_ontologies[i] = j
  
  
import pandas as pd
# Get all unique GO terms
all_go_terms = set()
for go_terms in filtered_ontologies.values():
    all_go_terms.update(go_terms)

# Create the DataFrame
df = pd.DataFrame(0, index=filtered_ontologies.keys(), columns=sorted(all_go_terms))

# Fill the DataFrame with 1s where appropriate
for protein, go_terms in filtered_ontologies.items():
    df.loc[protein, go_terms] = 1
for key,val in filtered_ontologies.items():
  df.loc[key, "label_count"] = len(val)
  
df = df.sort_values(by="label_count", ascending=False)
df = df.drop(df[df['label_count'] == 0].index)


 
# Save the dataframe to a CSV file
df.to_csv('go_label.csv', index=True)
  


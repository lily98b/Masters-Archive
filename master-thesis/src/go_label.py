
from tqdm import tqdm
from os import walk
import os
import json
import numpy as np
from goatools.obo_parser import GODag


"""
Each protein's GO will be classified into 3 groups of [2,4,6] levels of gene ontology hierarchy and this happens only for molecular function!
"""

filepath = "/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/dataset/go/raw/files"
for (dirpath, dirnames, filenames) in walk(filepath):
  break

# Filter out non-JSON files
json_filenames = [filename for filename in filenames if filename.endswith(".json")]

# loading the go basic file containing the basic GO terms and structure
obodag = GODag("/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/go-basic.obo")

#31157/31813 is done
not_found = {}
os.chdir(filepath)
for file in tqdm(json_filenames):
  id = os.path.splitext(file)[0]
  with open(f"{file}", "r") as f:
    d = json.load(f)
    level_ =[]
    for i in d["rcsb_polymer_entity_annotation"]:
     if i["type"] == "GO":
      if "molecular_function" in [i['name'] for i in i['annotation_lineage']]:
       for i in i["annotation_lineage"]:
        try:
         levell = obodag[i["id"]].level
         if levell in [2, 4, 6]:
           name = i["name"]
           go_id = i["id"]
           id_ = (f"{name}",f"{go_id}",f"{levell}")
           level_.append(id_)
        except Exception as e:
         not_found[f"{id}"] = i['id']
  np.save(f"/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/dataset/go/go_level/{id}", np.array(level_))


import os
import numpy as np
from tqdm import tqdm
from Bio.PDB import *
from Bio import PDB

pdb_dir = "/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/ec_model/CLEAN/app/data/AF_clean" 
seq_dir = "/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/ec_model/CLEAN/app/data/embedding_30_new/sequence" 


#extracting contact map info of Ca-Ca atoms 
parser = PDB.PDBParser(QUIET=True)
var_len = []
for file in tqdm(os.listdir(pdb_dir)):
  id = file.split(".")[0]
  try:
   seq_len = len(np.load(seq_dir+f"/{id}.npy").item())
   structure = parser.get_structure('id', pdb_dir+f"/{id}.pdb")
   model = structure[0]
   ca_coords = []
   residue_ids = []
   for chain in model:
     for residue in chain:
       if residue.has_id("CA"):
         ca_coords.append(residue["CA"].get_coord())
         residue_ids.append(residue.get_id())
   ca_coords = np.array(ca_coords)

   #initialize contact map
   contact_map = np.zeros((len(ca_coords), len(ca_coords)))

   #calculate distances between Ca-Ca atoms
   threshold = 8.0
   for i in range(len(ca_coords)):
     contact_map[i][i] =1
     for j in range(i+1, len(ca_coords)):
       distance = np.linalg.norm(ca_coords[i] - ca_coords[j]) #calculating euclidean distance
       if distance <= threshold:
         contact_map[i][j] = 1 #symmetric
         contact_map[j][i] = 1 
   if seq_len != len(contact_map[0]):
     var_len.append(id)
   np.save(f"/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/ec_model/CLEAN/app/data/contact_map/{id}", contact_map)
  except Exception as e:
      print(e, id)
      continue
np.save("/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/ec_model/CLEAN/app/data/contact_map/differ/var", np.array(var_len))


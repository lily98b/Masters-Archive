import random 
from tqdm import tqdm
import torch
import os
for file in tqdm(os.listdir("/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/go_cd_hit/esm_emb/len_esm_1280_cdhit_0.5")):
  embedding = torch.load(f"/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/go_cd_hit/esm_emb/len_esm_1280_cdhit_0.5/{file}")[0]
  i = random.randint(25,40)
  drop_residues = int((embedding.shape[0]*i)/100)
  idx = torch.randperm(embedding.size(0))[:drop_residues]
  mask = torch.ones(embedding.size(0), dtype=torch.bool)
  mask[idx] = False
  emb_random_filtered = embedding[mask]
  torch.save(emb_random_filtered,f"/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/go_cd_hit/esm_emb/random_esm_1280_cdhit_0.5/{file}")
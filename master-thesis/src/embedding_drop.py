import random 
from tqdm import tqdm
import torch
import os
for file in tqdm(os.listdir("/PATH/to/esm_1280_cdhit_0.5")):
  embedding = torch.load(f"/PATH/to/esm_1280_cdhit_0.5/{file}")[0]
  i = random.randint(25,40)
  drop_residues = int((embedding.shape[0]*i)/100)
  idx = torch.randperm(embedding.size(0))[:drop_residues]
  mask = torch.ones(embedding.size(0), dtype=torch.bool)
  mask[idx] = False
  emb_random_filtered = embedding[mask]
  torch.save(emb_random_filtered,f"/PATH/to/random_esm_1280_cdhit_0.5/{file}")

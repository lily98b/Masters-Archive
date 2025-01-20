
import os
import math
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader


"""
Preparing data for the training
"""

class ProteinDataset(Dataset):

   """
   retrive the dataset's features and labels one sample at a time with Dataset.
   """
   def __init__(self, npy_file, embedding_dir):#instantiate the Dataset object


    """
    args
    npy_file = path to the data file, the file must be with .npy extension
    embedding_dir = path to the embedding directory, the files must be with .pt extension

    """

    self.embedding_dir = embedding_dir
    self.npy_file = np.load(npy_file, allow_pickle=True)

    self.protein = self.npy_file[:,0]
    self.label = self.npy_file[:,1:18].astype(float)



   def __len__(self):  #return number of samples in the dataset
    return len(self.protein)

   def __getitem__(self, idx): # load and return a sample from dataset at the given index idx.
    protein = os.path.join(self.embedding_dir, self.protein[idx] + ".pt")
    protein = torch.load(protein)[0]
    label = torch.tensor(self.label[idx])
    return protein, label




#in order to pass the sample in minibatches and reshuffle the data at every epoch to reduce overfitting with DataLoader

dataset = ProteinDataset(npy_file = npy_file ,embedding_dir= embedding_dir)



size = np.load(npy_file, allow_pickle=True).shape[0]
seed =42
torch.manual_seed(seed)
training_data, test_data = torch.utils.data.random_split(dataset, [math.floor(0.8 * size), size - math.floor(0.8 * size) ])


train_dataloader = DataLoader(training_data, batch_size=32, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=32, shuffle=True)
  

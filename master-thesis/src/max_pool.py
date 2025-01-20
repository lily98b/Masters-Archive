import torch 
def get_max_pool(embedding:torch.Tensor):
    
  """"
  The output embedding will have the same dimensionality as the model embedding representation(e.g. dim = 1*1280)
  Args
  embedding: vector representation of each amino acid of a sequence with dimensionality of :(1,sequence_length,embedding_size)
  the embedding input must be 3D (x,y,z)
  the out embedding is 3D too!
  """
  max_embedding = torch.max(embedding, dim=1)
  return max_embedding.values.unsqueeze(0)
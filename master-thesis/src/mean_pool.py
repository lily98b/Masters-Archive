import torch
def get_mean_pool(embedding: torch.Tensor):
    """"
    The output embedding will have the same dimensionality as the model embedding representation(e.g. dim = 1*1280)
    Args
    embedding: vector representation of each amino acid of a sequence with dimensionality of :(sequence_length,embedding_size)
    the embedding input must be 2D (x,y)
    the out embedding is 2D too!
    """
    mean_embedding = torch.mean(embedding, dim=0)
    return mean_embedding.unsqueeze(0)

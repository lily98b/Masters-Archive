from transformers import T5Tokenizer, T5EncoderModel
from torch.utils.data import DataLoader
import numpy as np 
from tqdm import tqdm
import torch
import re
import os


model_dir = "/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/ProstT5_model/ProstT5"
tokenizer_dir = "/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/ProstT5_model/ProstT5_tokenizer"
seq_dir = "/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/go_cd_hit/seq_0.5"
emb_save = "/fs/pool/pool-schwille-user/Frohn_Bela/Seraj-Kiana/ProteinEvolution/ProteinEvolver/thesis/embeddings/go/prost_embed"


"""getting embedding representation with ProstT5 model"""


# Load the tokenizer
tokenizer = T5Tokenizer.from_pretrained(tokenizer_dir, do_lower_case=False)
# Load the model
model = T5EncoderModel.from_pretrained(model_dir)
# cast to half-precision if GPU is available
#model.full() if device=='cpu' else model.half()
#move the model to both avail cudas
device = torch.device("cuda")
model = model.to(device)



torch.cuda.memory_cached()
#move all sequences to a list
sequences = []
name = []
for file in tqdm(os.listdir(seq_dir)):
  id = file.split(".")[0]
  sequence = np.load(os.path.join(seq_dir, file)).item()
  sequences.append(sequence)
  name.append(id)

#introduce white-space between all amino acids and replace all rare/ambiguous amino acids by X 
sequences = [" ".join(list(re.sub(r"[UZOB]", "X", sequence))) for sequence in sequences]



#tokenize the data with batch sizes, tokenization will be the end as 1 and padding 0 comming afterwards: [...,1,0,0,0]
ids = tokenizer.batch_encode_plus(sequences,
                                  add_special_tokens=True,
                                  padding="longest",
                                  return_tensors='pt')



tokens =ids['input_ids']



batch_size = 1
data_loader = DataLoader(tokens, batch_size=batch_size)

torch.cuda.memory_cached()

model.eval()  # Set model to evaluation mode
with torch.no_grad():  # Disable gradient computation
    for i, batch in tqdm(enumerate(tqdm(data_loader, leave=False))):
        attention_mask = torch.tensor(ids['attention_mask'][i]).unsqueeze(0).to(device)
        data = batch.to(device)
        embedding_repr = model(input_ids=data,attention_mask=attention_mask)
        embedd = embedding_repr.last_hidden_state.cpu()
        torch.save(embedd, emb_save+f"/{name[i]}.pt")
        del data  # Delete the data tensor
        torch.cuda.empty_cache()
        
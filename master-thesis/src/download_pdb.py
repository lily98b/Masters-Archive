import os
import requests
from tqdm import tqdm
not_found = []
def download_alphafold_structure(uniprot_id, output_directory):
    url = f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-model_v4.pdb"
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        output_path = os.path.join(output_directory, f"{uniprot_id}.pdb")
        with open(output_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
    else:
        not_found.append(uniprot_id)

#uniprot_ids = "/PATH/to/uniprot_ids_list"
#output_directory = "/PATH/to/output dir"

# Download structures
for uniprot_id in tqdm(uniprot_ids):
    download_alphafold_structure(uniprot_id, output_directory)

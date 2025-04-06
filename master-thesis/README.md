# Optimizing Learned Representations from Protein Language Models


### Project Motivation

Protein function annotation is essential for biomedical research and drug discovery, yet experimental methods are expensive and slow.  
Recent advances in **Protein Language Models (PLMs)** enable functional predictions using only sequence data, but these embeddings are high-dimensional and often require compression.

### Research Goal

This project investigates **dimensionality reduction strategies** for pretrained protein embeddings in the downstream task of **Gene Ontology (GO) function prediction**.

### Key Questions
- Understanding the patterns in vector representations obtained from PLMs
- How do pooling methods perform?
- Evaluating feature selections.
- Can we shorten embeddings (e.g., down to 60%) without hurting accuracy?
- Do learnable reduction layers keep the same performance?
- Compare performance of various layers of PLMs.

### Key Findings

- Mean pooling consistently outperforms max pooling
- 60% of embedding size retains strong GO prediction performance
- Learnable reduction layers help adapt representations
- The representations from the deeper layers of PLM seemed to have similar performancee to the earlier layers indicating the lack of generalization improvement.

### Research Impact

Our work highlights the **robustness and redundancy** in protein embeddings and suggests that better **pretraining objectives**, not just model size, are key to downstream success.


### Workflow Steps

1. Input Sequence Preparation
Description: Prepare the protein sequences to be processed by the PLMs.
Steps:
Collect and format protein sequences in FASTA files.
Organize the sequences into a directory or file structure for batch processing.
2. Sequence Representation Extraction with PLMs
Description: Use ESM, ProstT5 to convert sequences into feature-rich vector representations.
Steps:
Choose a PLM (ESM, ProstT5) and load its pretrained model.
Tokenize the sequences as required by the chosen PLM.
Pass the sequences through the model to extract embeddings (hidden states).
Save the extracted representations for downstream analysis.
3. Feature Selection
Description: Select relevant residues to downstream task of GO classification.
Steps:
Use a feature selection criterion (ASA, logit, random).
Apply the feature selection method to embeddings:
Eliminate residues.
Retain key residues based on the selected criterion.
Save the pruned representations for pooling.
4. Pooling
Description: Aggregate or summarize the selected features into a fixed-length vector.
Steps:
Choose a pooling strategy (average pooling, max pooling).
Implement the pooling operation over the selected residues.
Save the pooled representations for model training.
5. Model Training for GO Prediction
Description: Train a predictive model using the processed representations.
Steps:
Define the downstream task (GO term prediction).
Split the data into training, and test sets.
Choose a model architecture (feedforward neural network).
Train the model using the pooled representations:
Use loss functions (cross-entropy for classification).
Optimize hyperparameters (learning rate, regularization).
Evaluate model performance using metrics such as F1-score, precision, and recall.
6. Evaluation and Results
Description: Assess the model's performance and summarize results.
Steps:
Generate evaluation metrics for the test set.
Compare performance across different feature selection and pooling strategies.

 **Pipeline Flow**:  
 
`FASTA → Tokenizer → PLM → Feature Selection → Pooling → Classifier`

### Acknowledgements

This project was inspired in part by the work presented in the preprint:  
**[How to Extract Useful Features from Protein Language Models?](https://www.biorxiv.org/content/biorxiv/early/2024/02/14/2024.02.05.578959.full.pdf)**  
*(bioRxiv, 2024)*  
The insights from this paper helped shape the experimental design and evaluation focus of this thesis.


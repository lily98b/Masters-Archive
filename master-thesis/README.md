# Optimizing Learned Representations from Protein Language Models


### Project Motivation

Protein function annotation is essential for biomedical research and drug discovery, yet experimental methods are expensive and slow.  
Recent advances in **Protein Language Models (PLMs)** enable functional predictions using only sequence data, but these embeddings are high-dimensional and often require compression.

### Research Goal

This project investigates **dimensionality reduction strategies** for pretrained protein embeddings in the downstream task of **Gene Ontology (GO) function prediction**.

### Key Questions
- How does **pooling method** (mean vs max) impact performance?
- Can we **compress embeddings** (e.g., down to 60%) without hurting accuracy?
- Do **learnable reduction layers** improve generalization?
- Do **newer PLMs** outperform older ones?

### Key Findings

- **Mean pooling** consistently outperforms max pooling
- **60% of embedding size** retains strong GO prediction performance
- **Learnable reduction layers** help adapt representations
- Surprisingly, **newer PLMs don’t always outperform older ones** — generalization depends on architecture and pretraining

### Research Impact

Our work highlights the **robustness and redundancy** in protein embeddings and suggests that better **pretraining objectives**, not just model size, are key to downstream success.


### Workflow Steps

<br>

<p align="center">
  <img src="Architecture.jpg" width="400" height="200">
</p>



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

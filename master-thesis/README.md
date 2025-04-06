# Optimizing Learned Representations from Protein Language Models

### Project Motivation

Protein function annotation is essential for biomedical research and drug discovery, yet experimental methods are expensive and slow.  
Recent advances in **Protein Language Models (PLMs)** enable functional predictions using only sequence data, but these embeddings are high-dimensional and often require compression.

### Research Goal

This project investigates **dimensionality reduction strategies** for pretrained protein embeddings in the downstream task of **Gene Ontology (GO) function prediction**.

### Key Questions

- What patterns emerge in vector representations from PLMs?
- How do different pooling methods compare in performance?
- Is it feasible to reduce embedding dimensions (e.g., by 60%) without compromising accuracy?
- Do learnable reduction layers maintain performance levels?
- How do various layers of PLMs perform comparatively?

### Key Findings

- Mean pooling consistently outperforms max pooling.
- Reducing the embedding size by 60% still retains strong GO prediction performance.
- Learnable reduction layers help adapt representations to the task.
- Representations from deeper layers of PLMs performed similarly to earlier layers, indicating a lack of generalization improvement.

### Research Impact

Our work highlights the **robustness and redundancy** in protein embeddings and suggests that better **pretraining objectives**—not just model size—are key to downstream success.

---

### Workflow Steps

1. **Input Sequence Preparation**  
   Prepare protein sequences in FASTA format, organized into directories for batch processing.

2. **Sequence Representation Extraction with PLMs**  
   Use PLMs (e.g., ESM, ProtT5) to convert sequences into vector representations:
   - Load pretrained PLM model.
   - Tokenize sequences.
   - Extract hidden states and save them.

3. **Feature Selection**  
   Select relevant residues for the downstream task:
   - Apply ASA, logit, or random filtering.
   - Prune or retain key residues accordingly.

4. **Pooling**  
   Aggregate selected features into fixed-length vectors:
   - Use average or max pooling over residues.
   - Save the pooled representations.

5. **Model Training for GO Prediction**  
   Train a classifier on the pooled vectors:
   - Use feedforward neural networks.
   - Train/test split, cross-entropy loss.
   - Evaluate with F1-score, precision, and recall.

6. **Evaluation and Results**  
   Assess performance:
   - Compare across pooling and feature selection strategies.

➡️ **Pipeline Flow**:  
`FASTA → Tokenizer → PLM → Feature Selection → Pooling → Classifier`

---

### Acknowledgements

This project was inspired in part by the work presented in the preprint:  
**[How to Extract Useful Features from Protein Language Models?](https://www.biorxiv.org/content/biorxiv/early/2024/02/14/2024.02.05.578959.full.pdf)**  
*(bioRxiv, 2024)*  
The insights from this paper helped shape the experimental design and evaluation focus of this thesis.

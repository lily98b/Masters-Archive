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


### Research Impact

Our work highlights the robustness and redundancy in protein embeddings and suggests that better pretraining objectives—not just model size—are key to downstream success.

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


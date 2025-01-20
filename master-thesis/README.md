# Optimization of Deep Learning-Based Protein Representations 

Proteins are essential macromolecules that play an important role in the structure, function, and regulation of cells and tissues in living organisms. Their diverse roles make understanding and annotation of protein functions a critical area of research. However, traditional experimental approaches for annotating protein functions require significant time and resources. Recent advancements in computational biology, particularly the application of Large pretrained protein language models (PLMs),
have improved protein function and structure prediction from sequences via transfer learning, in
which representations from PLMs
are repurposed for downstream tasks.
The representations derived from PLMs are high-dimensional vectors that, for some subsequent training tasks, require reduction of dimensionality. Currently, the predominant methods for this purpose are mean and max pooling; however, their effectiveness lacks a clear justification, and there may be more promising alternatives available. This thesis explores multiple strategies to compactly represent protein sequences and evaluates their performance in the downstream task of predicting Gene Ontology (GO) functions.
The experiment demonstrates that the downstream task of (GO) prediction benefits from protein language model-based representations. In particular, these representations maintain consistent evaluation results even when trained on 60\% of the protein sequence representation, rather than the entire sequence. The study finds that mean pooling outperforms max pooling in this context. However, when feature reduction layers are integrated into the downstream task model architecture, the input representations become fine-tuned to the task, leading to equal performance for models trained on representations from both mean and max pooling methods. Interestingly, representations derived from an improved protein language model architecture do not enhance the downstream task performance. In fact, they perform worse than the low-level features learned early in pre-training, indicating the need for more effective pre-training of PLMs.


# Workflow Steps

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

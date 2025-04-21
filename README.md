# Genomic Sequence Classification with HMM and CNN

A comparative machine learning project that models DNA sequences using both interpretable probabilistic models (Hidden Markov Models) and high-performance deep learning models (Convolutional Neural Networks).

---

## 🧬 Problem Statement

Given synthetic genomic sequences of fixed length (200 base pairs), the goal is to predict the correct class label (0–3) associated with embedded motif-like patterns. This task mimics real-world challenges in DNA motif detection and functional sequence classification.

---

## 🔍 Dataset

- **Type**: Synthetic sequences (A, C, G, T)
- **Length**: Fixed at 200bp per sequence
- **Labels**: 4 balanced classes (0, 1, 2, 3)
- **Split**: 
  - Train: 38,000 sequences
  - Validation: 1,000 sequences
  - Test: 1,000 sequences

---

## ⚙️ Approach

Two fundamentally different models were used:

### 1. Hidden Markov Models (HMM)
- One `CategoricalHMM` trained per class
- Predicts based on highest log-likelihood
- Emission and transition matrices provide interpretability

### 2. Convolutional Neural Networks (CNN)
- One-hot encoded input sequences (200, 4)
- Conv1D → MaxPool → Dropout → Dense → Softmax
- Captures local motifs automatically

---

## 📈 Results Summary

| Model | Test Accuracy | Notes |
|-------|---------------|-------|
| HMM   | ~90%          | Interpretable, lower complexity |
| CNN   | ~97%**     | Best performance, scalable |

- CNN significantly outperforms HMM in generalization and accuracy
- HMM provides interpretable state transitions and emissions

---

## 🗂 Project Structure

```
genomic-sequence-classification-hmm-cnn/
├── notebooks/              # Jupyter notebooks
├── data/                   # Sample datasets (if shareable)
├── models/                 # Saved model files
├── results/                # Confusion matrices, loss plots
├── README.md
├── requirements.txt
├── .gitignore
```

---

## ▶️ How to Run

1. Clone the repo  
```bash
git clone https://github.com/yourusername/genomic-sequence-classification-hmm-cnn.git
cd genomic-sequence-classification-hmm-cnn
```

2. Install dependencies  
```bash
pip install -r requirements.txt
```

3. Open the notebooks in `notebooks/` and run cells

---

## 📦 Dependencies

- numpy
- pandas
- scikit-learn
- hmmlearn
- tensorflow / keras
- matplotlib / seaborn

All dependencies are listed in `requirements.txt`.

---

## 📌 Future Work

- Try Transformers (e.g., DNABERT)
- Add real genomic datasets (ENCODE, ChIP-seq)
- Use hybrid HMM-CNN approaches
- Integrate sequence visualization tools

---

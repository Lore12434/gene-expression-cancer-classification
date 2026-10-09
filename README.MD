# Interpretable Pan-Cancer Classification via Sparse Elastic-Net Biomarker Discovery

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Accuracy](https://img.shields.io/badge/Test%20Accuracy-100%25-brightgreen.svg)]()
[![Dimensionality Reduction](https://img.shields.io/badge/Feature%20Reduction-99.82%25-success.svg)]()

An end-to-end machine learning pipeline that resolves the **curse of dimensionality** ($n \gg m$) in transcriptomic pan-cancer analysis. By mapping anonymized UCI RNA-Seq features back to official TCGA gene symbols and applying a custom sparse Elastic Net feature selection strategy, this project compresses **20,531 gene features down to 39 biologically verified biomarkers** (a **99.82% reduction**) while achieving **100% classification accuracy** on an independent test set across 5 primary cancer types.

---

## Visual Overview

| t-SNE Clustering (Latent Space Separation) | Final Evaluation (Test Set Confusion Matrix) |
| :---: | :---: |
| ![t-SNE Projection](reports/figures/tsne_plot.png) | ![Confusion Matrix](reports/figures/confusion_matrix.png) |
| *Clear separation among the 5 cancer classes prior to linear modeling.* | *Perfect generalization ($N=241$) using only the 39 extracted genes.* |

---

## Table of Contents
- [Clinical & Dataset Overview](#clinical--dataset-overview)
- [Methodology & Architecture](#methodology--architecture)
  - [1. Feature Reconstruction](#1-feature-reconstruction)
  - [2. Exploratory Dimensionality Reduction](#2-exploratory-dimensionality-reduction)
  - [3. Sparse Feature Selection (Elastic Net)](#3-sparse-feature-selection-elastic-net)
- [Benchmark Results](#benchmark-results)
- [Scientific & Clinical Validation](#scientific--clinical-validation)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Data Acquisition & Placement](#data-acquisition--placement)
  - [Running the Pipeline via CLI](#running-the-pipeline-via-cli)
  - [Notebook Workflow](#notebook-workflow)
- [License](#license)

---

## Clinical & Dataset Overview

This project analyzes the [UCI Gene Expression Cancer RNA-Seq Dataset](https://archive.ics.uci.edu/dataset/401/gene+expression+cancer+rna+seq), sampled from [The Cancer Genome Atlas (TCGA)](https://www.cancer.gov/ccg/research/genome-sequencing/tcga) Pan-Cancer project:

* **Samples:** $m = 801$ patients (Train: $560$, Test: $241$ via a stratified 70/30 split).
* **Initial Dimensionality:** $n = 20,531$ genes (Illumina HiSeq RNA-Seq V2).
* **Target Classes (5 Cancer Types):**
  * `BRCA`: Breast Invasive Carcinoma
  * `KIRC`: Kidney Renal Clear Cell Carcinoma
  * `LUAD`: Lung Adenocarcinoma
  * `PRAD`: Prostate Adenocarcinoma
  * `COAD`: Colon Adenocarcinoma

---

## Methodology & Architecture

```
Raw TCGA / UCI RNA-Seq (20,531 features)
       │
       ▼
Feature Mapping (gene_0...gene_n ➔ Official Gene Symbols)
       │
       ▼
Elastic Net Logistic Regression (SAGA solver, L1/L2 Grid Search)
       │
       ▼
Weight Matrix Extraction & Dynamic Thresholding:
       Threshold = (|W|_max - |W|_min) / 2
       │
       ▼
39 Discovered Gene Biomarkers (99.82% feature reduction)
       │
       ▼
StandardScaler + Logistic Regression Pipeline ➔ 100% Test Accuracy
```

### 1. Feature Reconstruction
The UCI RNA-Seq dataset labels genes generically (`gene_0`, `gene_1`, etc.), stripping all biological meaning. We extracted the original gene annotation header from the TCGA Pan-Cancer dataset (`unc.edu_PANCAN_IlluminaHiSeq_RNASeqV2.geneExp.tsv` hosted on Synapse: `syn4301332`) and re-mapped all 20,531 columns to their standard symbols (`SYMBOL|ENTREZ_ID`).

### 2. Exploratory Dimensionality Reduction
Using 2D t-SNE and PCA, we observed that global transcriptomic profiles separate into discrete, low-dimensional clusters per tumor origin. However, PCA-based features obscure biological interpretability ("black-box" components).

### 3. Sparse Feature Selection (Elastic Net)
To achieve an interpretable "white-box" model:
1. An **Elastic-Net Logistic Regression** model was optimized over parameter space ($C, \ell_1\text{-ratio}$) using randomized cross-validation:
   $$\min_{w} \left\{ -\frac{1}{m}\sum_{i=1}^{m} \log P(y^{(i)} \mid x^{(i)}; w) + \lambda \left[ \alpha \|w\|_1 + \frac{1 - \alpha}{2} \|w\|_2^2 \right] \right\}$$
2. From the coefficient matrix $W \in \mathbb{R}^{K \times D}$ ($K=5$ classes, $D=20,531$ genes), we eliminated all features where $w_j = 0$ across all classes.
3. We calculated the maximum absolute weight per remaining feature across all classes:
   $$S_j = \max_{k \in \{1 \dots K\}} |W_{k, j}|$$
4. We applied a dynamic median-range filter:
   $$\text{Threshold} = \frac{S_{\max} - S_{\min}}{2}$$
   Features with $S_j > \text{Threshold}$ were retained.

This reduced the feature space from **20,531** to **39 key predictive genes**.

---

## Benchmark Results

### 1. Feature Space Comparison (Full vs. Reduced)

| Stage | Features ($n$) | Reduction (%) | Logistic Regression (CV) | SVC (CV) | Random Forest (OOB) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Raw Data** | 20,531 | 0.00% | — | — | 99.63% |
| **PCA (95% Var)** | Latent PCs | N/A | 99.82% | 99.11% | 94.81% |
| **Elastic Net Selection** | **39** | **99.82%** | **99.82%** | **99.64%** | **99.28%** |

### 2. Final Test Set Evaluation (Reduced 39 Features, $N=241$)

All models trained exclusively on the **39 selected genes** achieved **perfect classification** on unseen test data:

| Model | Test Accuracy | Test Samples Correct | Misclassifications |
| :--- | :---: | :---: | :---: |
| **Logistic Regression (StandardScaler)** | **100.0%** | **241 / 241** | **0** |
| **Support Vector Classifier (SVC)** | **100.0%** | **241 / 241** | **0** |
| **Random Forest Classifier** | **100.0%** | **241 / 241** | **0** |

```
              Test Set Confusion Matrix (39 Biomarkers)
              
                 Pred: KIRC   BRCA   PRAD   LUAD   COAD
      Actual:
      KIRC (n=41)     41      0      0      0      0
      BRCA (n=90)      0     90      0      0      0
      PRAD (n=42)      0      0     42      0      0
      LUAD (n=40)      0      0      0     40      0
      COAD (n=28)      0      0      0      0     28
```

---

## Scientific & Clinical Validation

The 39 genes extracted completely match established clinical diagnostic IHC panels, oncology biomarkers, and targeted therapeutics:

| Gene Selected | Protein / Alias | Cancer Type | Diagnostic / Therapeutic Significance |
| :--- | :--- | :---: | :--- |
| **`KLK3`** | PSA | **PRAD** | Worldwide gold-standard serum biomarker for prostate cancer screening and monitoring ([PMID: 15302825](https://pubmed.ncbi.nlm.nih.gov/15302825/)). |
| **`KLK2`** | Human Kallikrein 2 | **PRAD** | Activates pro-PSA; highly specific tissue marker for prostate adenocarcinoma ([PMID: 11266155](https://pubmed.ncbi.nlm.nih.gov/11266155/)). |
| **`TMEFF2`** | Tomoregulin-2 | **PRAD** | Androgen-regulated gene under study as a prostate-specific therapeutic target ([PMID: 11751478](https://pubmed.ncbi.nlm.nih.gov/11751478/)). |
| **`NKX2-1`** | TTF-1 | **LUAD** | Pathological gold-standard IHC marker confirming primary lung origin in metastatic lesions ([PMID: 21677561](https://pubmed.ncbi.nlm.nih.gov/21677561/)). |
| **`NAPSA`** | Napsin A | **LUAD** | Primary aspartic protease diagnostic partner to TTF-1 for lung adenocarcinoma typing ([PMID: 21677561](https://pubmed.ncbi.nlm.nih.gov/21677561/)). |
| **`SFTPB/C/D`** | Surfactants B, C, D | **LUAD** | Specific to alveolar Type II epithelial cells; retained in lung lineage adenocarcinomas ([PMID: 17012351](https://pubmed.ncbi.nlm.nih.gov/17012351/)). |
| **`ROS1`** | ROS1 Kinase | **LUAD** | Actionable oncogenic fusion target for FDA-approved TKIs (Crizotinib, Entrectinib) ([NCBI: NBK585049](https://www.ncbi.nlm.nih.gov/books/NBK585049/)). |
| **`GATA3`** | GATA-3 | **BRCA** | Master regulator of luminal breast differentiation; diagnostic IHC marker with >90% sensitivity ([PMID: 25906123](https://pubmed.ncbi.nlm.nih.gov/25906123/)). |
| **`SCGB2A2`** | Mammaglobin A | **BRCA** | Secretoglobin marker used to detect micrometastases and circulating breast cancer cells ([PMID: 10411107](https://pubmed.ncbi.nlm.nih.gov/10411107/)). |
| **`PRLR`** | Prolactin Receptor | **BRCA** | Central receptor in mammary differentiation and hormone-dependent breast carcinoma ([PMID: 18451167](https://pubmed.ncbi.nlm.nih.gov/18451167/)). |
| **`CDX1`** | Caudal Type Homeobox 1| **COAD** | Lineage-specific transcription factor governing intestinal epithelial differentiation ([PMID: 19196968](https://pubmed.ncbi.nlm.nih.gov/19196968/)). |
| **`HNF1B`** | HNF-1 Beta | **KIRC** | Sensitive and specific regulator for clear cell renal cell carcinoma lineage typing ([PMID: 15643446](https://pubmed.ncbi.nlm.nih.gov/15643446/)). |

*Full analysis available in [`reports/clinical proof for biomarkers.md`](reports/clinical%20proof%20for%20biomarkers.md).*

---

## Repository Structure

```
gene-expression-cancer-classification/
├── data/
│   ├── features_weights/       # Serialized Elastic Net coefficients
│   │   └── numpy_features_weights_arr.npy
│   ├── processed/              # Filtered, re-mapped, train/test splits (.csv)
│   └── raw/                    # UCI data and TCGA annotation mapping (.csv, .tsv)
├── models/                     # Trained models and final pipelines
│   ├── elastic_net_log_reg
│   ├── final_pipeline_model    # Best deployed pipeline (StandardScaler + LogReg)
│   ├── logistic_regression_pip_39
│   ├── random_forest_39
│   └── SVC_pip_39
├── notebooks/                  # Step-by-step exploration and modeling
│   ├── 01_eda_and_dim_reduction.ipynb
│   ├── 02_preprocessing_and_feature_selection.ipynb
│   └── 03_model_evaluation.ipynb
├── reports/                    # Clinical documentation and plots
│   ├── clinical proof for biomarkers.md
│   └── figures/
│       ├── confusion_matrix.png
│       └── tsne_plot.png
├── src/                        # Modular production code
│   ├── __init__.py
│   ├── data_loader.py          # Data ingestion, gene re-mapping, train/test splits
│   ├── preprocessing.py        # Feature matrix thresholding & dataset reduction
│   ├── train.py                # Pipeline fitting and serialization
│   └── evaluate.py             # Test set evaluation and confusion matrix generation
├── requirements.txt            # Python dependencies
└── README.md
```

---

## Getting Started

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/gene-expression-cancer-classification.git
   cd gene-expression-cancer-classification
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Data Acquisition & Placement

1. Download the RNA-Seq Pan-Cancer dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/401/gene+expression+cancer+rna+seq).
2. Download the TCGA gene expression annotation file (`unc.edu_PANCAN_IlluminaHiSeq_RNASeqV2.geneExp.tsv`) from [Synapse (ID: syn4301332)](https://www.synapse.org/#!Synapse:syn4301332).
3. Place all raw files in `data/raw/`:
   ```
   data/raw/
   ├── data.csv
   ├── labels.csv
   └── unc.edu_PANCAN_IlluminaHiSeq_RNASeqV2.geneExp.tsv
   ```

### Running the Pipeline via CLI

Execute the modular source pipeline directly from the root directory:

1. **Preprocess data and split into train/test sets:**
   ```bash
   python -c "from src.data_loader import load_and_save_data; load_and_save_data(test_size=0.3)"
   ```

2. **Train the final pipeline on the 39 extracted biomarkers:**
   ```bash
   python -m src.train
   ```

3. **Evaluate performance on the test set and generate the confusion matrix:**
   ```bash
   python -m src.evaluate
   ```

### Notebook Workflow

You can also run through the notebooks interactively:
1. `notebooks/01_eda_and_dim_reduction.ipynb`: EDA, null-value checks, t-SNE latent projection.
2. `notebooks/02_preprocessing_and_feature_selection.ipynb`: Model benchmarking, PCA vs. Isomap, Elastic Net optimization, coefficient matrix extraction, and dynamic thresholding.
3. `notebooks/03_model_evaluation.ipynb`: Cross-validation on the 39-feature subset and test-set verification across Logistic Regression, SVC, and Random Forest.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
```

***

### Notes for your repository:
1. Replace `<your-username>` in the clone URL with your actual GitHub username.
2. Ensure `reports/figures/tsne_plot.png` and `reports/figures/confusion_matrix.png` match the exact casing and filenames in your directory so GitHub renders the markdown images immediately.
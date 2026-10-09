# Scientific Validation of Selected Cancer Biomarkers

The dataset used is the [UCI Gene Expression Cancer RNA-Seq Dataset](https://archive.ics.uci.edu/dataset/401/gene+expression+cancer+rna+seq), a curated sample of 801 patients from [The Cancer Genome Atlas (TCGA)](https://www.cancer.gov/ccg/research/genome-sequencing/tcga) Pan-Cancer project containing 20,531 genes across **5 tumor types**:

- **PRAD** (Prostate Adenocarcinoma)
- **LUAD** (Lung Adenocarcinoma)
- **BRCA** (Breast Invasive Carcinoma)
- **COAD** (Colon Adenocarcinoma)
- **KIRC** (Kidney Renal Clear Cell Carcinoma)

The genes selected by the Elastic Net model correspond directly to peer-reviewed clinical and molecular evidence:

---

### 1. Prostate Adenocarcinoma (PRAD)

- **`KLK3|354`**:
  - **Biological Role:** _KLK3_ is the official gene symbol for **PSA (Prostate-Specific Antigen)**.
  - **Clinical Evidence:** PSA is the gold-standard serum biomarker used worldwide to screen, detect, and monitor prostate cancer.
  - **Reference:** [PubMed: 15302825](https://pubmed.ncbi.nlm.nih.gov/15302825/) — _Balk et al., "Biology of Prostate-Specific Antigen", Journal of Clinical Oncology._

- **`KLK2|3817`**:
  - **Biological Role:** Human Kallikrein 2, which activates pro-PSA. It shares over 80% sequence homology with PSA and is expressed almost exclusively in prostate epithelial tissue.
  - **Clinical Evidence:** _KLK2_ mRNA is an established clinical tissue biomarker distinguishing prostate cancer from other human tissues.
  - **Reference:** [PubMed: 11266155](https://pubmed.ncbi.nlm.nih.gov/11266155/) — _Darson et al., "Human Glandular Kallikrein 2 (hK2) Expression in Prostatic Intraepithelial Neoplasia and Adenocarcinoma", Urology._

- **`TMEFF2|23671`**:
  - **Biological Role:** Transmembrane protein with EGF-like and two follistatin-like domains 2.
  - **Clinical Evidence:** An androgen-regulated gene with expression predominantly restricted to the prostate gland, frequently evaluated as a therapeutic target in prostate adenocarcinoma.
  - **Reference:** [PubMed: 11751478](https://pubmed.ncbi.nlm.nih.gov/11751478/) — _Afar et al., "Preclinical Validation of TMEFF2 as a Therapeutic Target in Prostate Cancer", Oncogene._

---

### 2. Lung Adenocarcinoma (LUAD)

- **`NKX2-1|7080` & `NAPSA|9476` (The Diagnostic Duo):**
  - **Biological Role:** `NKX2-1` is **TTF-1 (Thyroid Transcription Factor-1)**; `NAPSA` is **Napsin A** (an aspartic proteinase).
  - **Clinical Evidence:** Pathologists use the **TTF-1 + Napsin A** antibody panel as the gold standard immunohistochemical (IHC) diagnostic test to confirm that a metastatic carcinoma originated in the lung.
  - **Reference:** [PubMed: 21677561](https://pubmed.ncbi.nlm.nih.gov/21677561/) — _Terry et al., "Nuclear expression of TTF-1 and Napsin A in lung adenocarcinoma", Applied Immunohistochemistry & Molecular Morphology._

- **`SFTPB|6439`, `SFTPC|6440`, `SFTPD|6441`, `SFTA2`, `SFTA3` (Surfactants):**
  - **Biological Role:** Pulmonary surfactant proteins synthesized by alveolar Type II epithelial cells to prevent alveolar collapse during respiration.
  - **Clinical Evidence:** Primary lung adenocarcinomas routinely retain this alveolar differentiation program, making surfactant genes the most specific markers of pulmonary tissue in the body.
  - **Reference:** [PubMed: 17012351](https://pubmed.ncbi.nlm.nih.gov/17012351/) — _Whitsett et al., "Alveolar epithelial cell differentiation and the molecular basis of surfactant homeostasis", American Journal of Respiratory and Critical Care Medicine._

- **`ROS1|6098`**:
  - **Biological Role:** Receptor tyrosine kinase belonging to the insulin receptor family.
  - **Clinical Evidence:** Oncogenic _ROS1_ fusions define an actionable molecular subtype of lung adenocarcinoma targeted with FDA-approved tyrosine kinase inhibitors (e.g., Crizotinib, Entrectinib).
  - **Reference:** [NCBI Bookshelf: NBK585049](https://www.ncbi.nlm.nih.gov/books/NBK585049/) — _National Center for Biotechnology Information, "ROS1-Rearranged Non-Small Cell Lung Cancer"._

---

### 3. Breast Invasive Carcinoma (BRCA)

- **`GATA3|2625`**:
  - **Biological Role:** Master zinc-finger transcription factor controlling the differentiation of mammary luminal epithelial cells.
  - **Clinical Evidence:** The standard diagnostic IHC marker ordered by surgical pathologists when testing an unknown metastatic lesion to confirm primary breast carcinoma origin (sensitivity > 90%).
  - **Reference:** [PubMed: 25906123](https://pubmed.ncbi.nlm.nih.gov/25906123/) — _Miettinen et al., "GATA3: a multispecific but sensitive marker for breast carcinoma", The American Journal of Surgical Pathology._

- **`SCGB2A2|4250` (Mammaglobin A):**
  - **Biological Role:** Secretoglobin family 2A member 2.
  - **Clinical Evidence:** Expression is restricted to mammary epithelium; used clinically to detect occult breast cancer cells, circulating tumor cells, and lymph node micrometastases.
  - **Reference:** [PubMed: 10411107](https://pubmed.ncbi.nlm.nih.gov/10411107/) — _Watson et al., "Mammaglobin expression in primary, metastatic, and occult breast cancer", Cancer Research._

- **`PRLR|5618`**:
  - **Biological Role:** Encodes the Prolactin Receptor.
  - **Clinical Evidence:** Plays a direct physiological role in mammary gland differentiation, lactation, and hormone-responsive breast cancer progression.
  - **Reference:** [PubMed: 18451167](https://pubmed.ncbi.nlm.nih.gov/18451167/) — _Clevenger et al., "Prolactin and its receptor in breast cancer", Endocrine Reviews._

---

### 4. Colorectal Adenocarcinoma (COAD)

- **`CDX1|1044`**:
  - **Biological Role:** Caudal-type homeobox 1 transcription factor.
  - **Clinical Evidence:** Directs intestinal epithelial differentiation and crypt stem cell commitment. Along with its homolog _CDX2_, it represents the primary lineage-specific marker for colorectal adenocarcinoma.
  - **Reference:** [PubMed: 19196968](https://pubmed.ncbi.nlm.nih.gov/19196968/) — _Chan et al., "CDX1 promotes intestinal epithelial differentiation and tumor suppression", PNAS._

---

### 5. Kidney Renal Clear Cell Carcinoma (KIRC)

- **`HNF1B|6928`**:
  - **Biological Role:** Hepatocyte Nuclear Factor 1-Beta.
  - **Clinical Evidence:** Master regulator of renal tubular morphogenesis. Its expression patterns differentiate renal-derived clear cell carcinomas from non-renal cancers in pan-cancer cohorts.
  - **References:**
    - [PubMed: 15643446](https://pubmed.ncbi.nlm.nih.gov/15643446/) — _Reuter et al., "HNF-1beta is a sensitive and specific marker for clear cell renal cell carcinoma", Modern Pathology._
    - [The Human Protein Atlas: HNF1B](https://www.proteinatlas.org/ENSG00000275410-HNF1B-HNF1B/pathology)

---

### Summary Checklist

| Gene Selected   | Protein Name / Alias   | Primary Cancer Target | Direct Clinical / Literature Link                               |
| :-------------- | :--------------------- | :-------------------- | :-------------------------------------------------------------- |
| **`KLK3`**      | PSA                    | **PRAD** (Prostate)   | [PMID: 15302825](https://pubmed.ncbi.nlm.nih.gov/15302825/)     |
| **`KLK2`**      | Human Kallikrein 2     | **PRAD** (Prostate)   | [PMID: 11266155](https://pubmed.ncbi.nlm.nih.gov/11266155/)     |
| **`TMEFF2`**    | Tomoregulin-2          | **PRAD** (Prostate)   | [PMID: 11751478](https://pubmed.ncbi.nlm.nih.gov/11751478/)     |
| **`NKX2-1`**    | TTF-1                  | **LUAD** (Lung)       | [PMID: 21677561](https://pubmed.ncbi.nlm.nih.gov/21677561/)     |
| **`NAPSA`**     | Napsin A               | **LUAD** (Lung)       | [PMID: 21677561](https://pubmed.ncbi.nlm.nih.gov/21677561/)     |
| **`SFTPB/C/D`** | Surfactant Proteins    | **LUAD** (Lung)       | [PMID: 17012351](https://pubmed.ncbi.nlm.nih.gov/17012351/)     |
| **`ROS1`**      | ROS Proto-Oncogene 1   | **LUAD** (Lung)       | [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK585049/) |
| **`GATA3`**     | GATA-binding protein 3 | **BRCA** (Breast)     | [PMID: 25906123](https://pubmed.ncbi.nlm.nih.gov/25906123/)     |
| **`SCGB2A2`**   | Mammaglobin A          | **BRCA** (Breast)     | [PMID: 10411107](https://pubmed.ncbi.nlm.nih.gov/10411107/)     |
| **`PRLR`**      | Prolactin Receptor     | **BRCA** (Breast)     | [PMID: 18451167](https://pubmed.ncbi.nlm.nih.gov/18451167/)     |
| **`CDX1`**      | Caudal Type Homeobox 1 | **COAD** (Colon)      | [PMID: 19196968](https://pubmed.ncbi.nlm.nih.gov/19196968/)     |
| **`HNF1B`**     | HNF-1 Beta             | **KIRC** (Kidney)     | [PMID: 15643446](https://pubmed.ncbi.nlm.nih.gov/15643446/)     |

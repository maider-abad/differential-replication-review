# Model Reuse Under Deployment Constraints: A Review of Differential Replication Methods

This repository accompanies the article:

> **Model reuse under deployment constraints: a review of differential replication methods**

It contains the dataset generated during the **systematic literature review** of differential replication methods, as described in the methodology section of the paper.  

---

## 📂 Repository Contents

- **`literature_review_analysis.xlsx`**  
  A structured spreadsheet documenting the entire review and coding process.  
  It includes the following fields for each study:

  - **Title**  
  - **Year**  
  - **Link**  
  - **Summary** (3–4 lines)  
  - **Differential Replication Technique?** (Yes/No and justification)  
  - **Keywords**  
  - **Normalized Numeric Access to Model**  
  - **Numeric Access to Model**  
  - **Comments on Access to Model**  
  - **Normalized Numeric Access to Training Data**  
  - **Numeric Access to Training Data**  
  - **Comments on Access to Training Data**  
  - **Applications** (specific applications discussed)  
  - **Main Methodology**  
  - **DL or ML?**  
  - **Main Application**  
  - **Task**  
  - **Use Case**  
  - **Domain**  
  - **Complexity of the Methodology**  
  - **Comments on Model Complexity**  
  - **Parameters (M)**  

---

## 🔍 Methodology Overview

The literature review followed a **systematic review process** informed by PRISMA 2020 guidelines, with adaptations for the exploratory scope of the topic.  

### 1. Identification
- Comprehensive searches across **PubMed, IEEE Xplore, ACM Digital Library, and ScienceDirect**.  
- Queries combined targeted keywords and related concepts, including:  
  *“differential replication”*, *“model extraction”*, *“knowledge transfer”*, *“meta-learning”*, *“model compression”*, *“teacher-student network”*, *“distillation”*, *“quantization”*, and *“few-shot learning”*.  
- Citation chaining expanded the corpus iteratively.

### 2. Screening
- **Titles and abstracts** reviewed to exclude irrelevant or low-quality publications.  
- Non-peer-reviewed content, editorials, and short commentaries were removed.  
- Resulted in ~100 candidate articles.

### 3. Examination
- **Full-text review** applied two eligibility criteria:  
  1. The study generated a new model from an existing one.  
  2. The task and domain remained unchanged.  
- Reduced to 85 eligible articles.

### 4. Inclusion
- Retained only **methodologically detailed studies** proposing or evaluating a specific technique.  
- Excluded surveys and conceptual overviews.  
- **Final corpus: 75 articles** (with 10 additional studies used for context).

---

## 📊 Data Use

The spreadsheet can be used to:
- Replicate the review process.  
- Explore methodological patterns across studies.  
- Build comparative analyses of replication strategies under deployment constraints.  

Due to methodological heterogeneity, no meta-analysis of effect sizes was performed. Instead, we provide structured descriptors to enable **cross-study synthesis**.

---

## 📝 License

This repository is distributed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.  
You are free to share and adapt the material for any purpose, even commercially, provided that appropriate credit is given.

For more details, see: [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)

---

## 📑 Citation

If you use this dataset or methodology, please cite the following work (pre-publication reference):

```bibtex
@unpublished{abad2025differential,
  title     = {Model reuse under deployment constraints: a review of differential replication methods},
  author    = {Abad, Maider and Nin, Jordi and Unceta, Irene},
  year      = {2025},
  note      = {Manuscript in preparation}
}

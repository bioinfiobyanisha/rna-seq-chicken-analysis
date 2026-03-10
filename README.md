# Multi-Species Genome Annotation and Comparative Genomics

## Project Overview
This repository contains a bioinformatics workflow for genome assembly refinement, gene annotation transfer, and comparative genomic analysis across multiple livestock species. The project focuses on identifying conserved and species-specific genes and assembling Y chromosome segments in buffalo breeds.

The workflow integrates reference-guided scaffolding, gene annotation transfer, RNA-seq analysis, and comparative genomics visualization.

---

# Objectives

- Perform genome annotation transfer across species
- Identify common and species-specific genes
- Assemble Y chromosome segments in buffalo breeds
- Conduct comparative genomics analysis across livestock genomes

---

# Species Included

- Buffalo (Bangladesh, Jafarabadi, Murrah)
- Pig
- Goat
- Sheep

---

# Workflow Overview

## Genome Annotation Pipeline
![Genome Annotation Pipeline](https://github.com/user-attachments/assets/54750f2d-7eb6-451e-a75b-cb9c54fced90)



## 1 Genome Preparation
Download reference genomes and annotation files from public databases.

Input files:
- Genome FASTA
- Annotation GFF3 / GTF

---

## 2 Reference Guided Scaffolding

Tool used:
RagTag

Purpose:
Improve genome structure using a closely related reference genome.

Example: ragtag.py scaffold reference.fa target.fa

Output:
Chromosome-level scaffolds

---

## 3 Gene Annotation Transfer

Tool used:
Liftoff

Purpose:
Transfer gene annotations from reference genome to target genome.

Example: liftoff target.fa reference.fa -g reference.gtf

Output:
New GTF annotation file for target genome

---

## 4 Genome Mapping

Tool used:
Minimap2

Purpose:
Map genome assemblies to reference chromosomes and identify chromosome-specific scaffolds.

Example: minimap2 -ax asm5 reference.fa genome.fa > alignment.sam

Output:
SAM alignment file

---

## 5 Y Chromosome Identification

Steps:
- Extract reference Y chromosome
- Identify scaffolds mapping to Y chromosome
- Perform reference-guided assembly

Results:

Bangladesh buffalo
- 528 Y-linked scaffolds
- ~8.85 Mb assembled Y segment

Jafarabadi buffalo
- 1163 Y-linked scaffolds
- ~11.8 Mb assembled Y segment

---

## 6 Comparative Gene Analysis

Tasks performed:

- Extract total gene counts
- Identify common genes across species
- Identify species-specific genes

Output files:
- Gene count tables
- Comparative gene lists

---

## 7 Data Visualization

Tool used:
UpSet Plot

Purpose:
Visualize gene overlap across species and breeds.

Output:
- Gene intersection visualization
- Breed-specific gene identification

---
# Repository Structure
multi-species-genome-annotation
│
├── scripts
│   ├── gene_count.py
│   └── upset_plot.py
│
├── week-01_dec-21.md
├── week-02_dec-28.md
├── week-03_jan-04.md
├── week-04_jan-11.md
├── week-05_jan-18.md
├── week-06_jan-25.md
├── week-07_feb-01.md
├── week-08_feb-07.md
├── week-09_feb-15.md
├── week-10_feb-22.md
├── week-11_mar-01.md
│── week-l2_mar-08.md
└── README.md

---

# Tools Used

- RagTag
- Liftoff
- Minimap2
- Python
- Linux command line
- Excel
- UpSetPlot

---

# Future Work

- Complete annotation for additional buffalo breeds
- Improve Y chromosome assembly quality
- Perform functional annotation
- Expand comparative genomics analysis

---

---

## Author & Affiliation
**Anisha Vishwakarma**  
MSc Biotechnology | Aspiring Bioinformatician  

**Affiliation:**  
National Institute of Animal Biotechnology (NIAB), Hyderabad  

**Supervisor:**  
Dr. Shailesh Sharma, Scientist F  

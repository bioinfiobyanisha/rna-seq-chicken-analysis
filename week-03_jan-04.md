# Week 3 – 4 January  
## RagTag and Liftoff Analysis

## Genome Dataset Overview
- Total chicken genomes analyzed: 45
  - 40 breeds
  - 5 isolates
- All 5 isolates are chromosome-level assembled
- Among the 40 breeds:
  - 20 have chromosome-level assemblies
  - 20 are not chromosome-level assembled

---

## Chromosome-Level Scaffolding Using RagTag

For genomes that were not chromosome assembled, chromosome-level
scaffolding was performed using **RagTag**.

### Reference and Target Selection
- Reference genome: **Red Jungle Fowl**
- Target genome: **Fayoumi** (genomic FASTA)

### Results
- RagTag scaffolding produced **34 chromosomes** in the Fayoumi assembly

### Validation
To validate chromosome consistency:
- RagTag was repeated using **White Leghorn** as the reference genome
- The Fayoumi genome again resulted in **34 chromosomes**
- This confirmed consistency across different reference genomes

---

## Gene Annotation Transfer Using Liftoff

### Data Preparation
- Downloaded and unzipped:
  - Red Jungle Fowl genomic FNA and GTF files
  - White Leghorn genomic FNA file

### Liftoff Execution
- Used **Red Jungle Fowl** as the reference genome
- Used **White Leghorn** as the target genome
- Successfully ran Liftoff on **chromosome 1**
- Annotation transfer completed successfully for this chromosome

---

## Liftoff on Fayoumi Genome

- Attempted to run Liftoff using Fayoumi as the target genome
- The process was terminated during execution, likely due to
  system resource limitations
- Planned strategy:
  - Retry Liftoff using a chromosome-wise approach
  - Alternatively, split the genome to reduce resource usage

---

## Current Status
✔ Chromosome-level scaffolding validated using RagTag  
✔ Liftoff successfully tested on White Leghorn (chromosome 1)  
✔ Identified system limitations and mitigation strategies  

---

## Plan for Next Week
- Perform chromosome-wise Liftoff on Fayoumi genome
- Optimize resource usage during annotation transfer
- Continue annotation generation for non-chromosome assembled breeds

# Week 10 – Buffalo Genome Assembly and Annotation (22 Feb)

## Objectives
- Perform genome assembly and annotation for buffalo breeds
- Generate annotation files for Bangladesh buffalo using reference-guided approaches

## Work Done

### Reference Genome Assessment
- The available reference breed **Murrah** is female and has a complete genome assembly with an available GTF file.
- The target breeds **Bangladesh** and **Jafrabadi** are male.

### Genome Assembly for Bangladesh Breed
- Since the Bangladesh breed did not have a chromosome-level genome assembly, reference-guided scaffolding was performed.
- **Male swamp buffalo chromosome FASTA** was used as the reference genome.
- **Bangladesh genomic FASTA** was used as the target genome.

### Reference-Guided Scaffolding
- The **RagTag** tool was applied to perform scaffolding.
- Chromosome-level output was generated.
- From the results, the real chromosomes were identified and compiled into a list.

Final chromosome set identified:
- **23 autosomes**
- **X chromosome**
- **Y chromosome**

### Y Chromosome Observation
- The **Y chromosome length was relatively small** in the assembled results.
- This occurs because:
  - The Y chromosome is **highly repetitive**
  - Some Y regions may partially map to **autosomes or the X chromosome**

Therefore, the Y chromosome sequence should be interpreted as a **reference-guided scaffolding output rather than a fully resolved biological assembly**.

### Annotation Transfer
- Downloaded the **male swamp buffalo GFF3 annotation file**
- Converted the GFF3 file into **GTF format**

### GTF File Correction
- The initial GTF file did not properly contain **gene features**
- The file was corrected to ensure proper **gene annotations**

### Liftoff Annotation Transfer
- Used the **male swamp buffalo GTF as the reference**
- Applied the **Liftoff tool** to transfer gene annotations

Result:
- **GTF annotation successfully generated for the Bangladesh buffalo genome**

## Outcome
- Bangladesh buffalo genome successfully scaffolded using RagTag
- Chromosome structure identified (23 autosomes + X + Y)
- Gene annotation transferred using Liftoff
- Final GTF annotation file generated for Bangladesh breed

## Next Steps
- Validate annotation quality
- Perform comparative genomic analysis with other buffalo breeds
- Proceed with annotation for **Jafrabadi buffalo**

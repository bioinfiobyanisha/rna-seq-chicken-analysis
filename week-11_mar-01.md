# Week 11 – Y Chromosome Identification and Assembly (1 March)

## Objectives
- Identify Y chromosome–linked scaffolds for Bangladesh and Jafarabadi buffalo breeds
- Perform reference-guided assembly of Y chromosome segments

## Work Done

### Y Chromosome Scaffold Identification
- Used the **male Swamp buffalo chromosome-level assembly** as the reference genome.
- Mapped genomic sequences of **Bangladesh** and **Jafarabadi** buffalo breeds to the reference genome using **Minimap2**.
- Generated alignment files in **SAM format**.

### Alignment Analysis
- Analyzed the alignment results to identify scaffolds mapping specifically to the **reference Y chromosome**.

Results:
- **Bangladesh breed:** 528 high-confidence Y-linked scaffolds identified.
- **Jafarabadi breed:** 1163 high-confidence Y-linked scaffolds identified.

### Reference-Guided Y Assembly
- Extracted the **reference Y chromosome sequence**.
- Performed **reference-guided assembly using RagTag** for both breeds separately.

### Assembly Results
- **Bangladesh breed:** ~8.85 Mb assembled Y-linked segment
- **Jafarabadi breed:** ~11.8 Mb assembled Y-linked segment

The Jafarabadi breed produced a comparatively larger Y chromosome segment than the Bangladesh breed.

## Outcome
- Successfully identified Y chromosome–linked scaffolds in both buffalo breeds.
- Generated preliminary Y chromosome assemblies using RagTag.

## Next Steps
- Perform validation and quality assessment of Y-linked assemblies
- Evaluate scaffold coverage and mapping consistency
- Integrate Y chromosome segments into downstream comparative genomic analysis

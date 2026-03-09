# Week 12 Progress Report (8 March)

## Y Chromosome Gene Identification and Comparative Analysis

After completing chromosome-level assembly for the Bangladesh and Jafarabadi buffalo genomes, Y chromosome gene annotation and comparative analysis were performed.

### Annotation Transfer

The cattle Y chromosome reference FASTA and GTF annotation files were downloaded.  
The Y chromosome sequence and corresponding annotations were extracted.

Using the **Liftoff tool**, gene annotations from the cattle Y chromosome were transferred to the assembled Y chromosome segments of:

- Bangladesh buffalo
- Jafarabadi buffalo

This process generated **GFF3 annotation files** for both breeds.

### Male-Specific Gene Identification

The resulting GFF3 files were examined to identify Y chromosome male-specific genes.

**Jafarabadi buffalo**

- SRY
- DDX3Y
- EIF1AY
- USP9Y

**Bangladesh buffalo**

- DDX3Y
- EIF1AY
- USP9Y
- RBMY
- ZFY

Gene coordinates were extracted and compiled into an Excel sheet comparing cattle, Bangladesh, and Jafarabadi annotations.

### Non-Coding Region Alignment

To analyze sequence conservation, the **non-coding regions of the cattle Y chromosome** were aligned with buffalo Y chromosome segments using **Minimap2**.

### Average Alignment Identity (per alignment block)

Cattle vs Bangladesh: **22.8%**  
Cattle vs Jafarabadi: **25.6%**

### Overall Non-Gene Region Identity

Cattle vs Bangladesh: **18.6%**  
Cattle vs Jafarabadi: **13.8%**

These results indicate that the **non-coding regions of the Y chromosome show relatively low sequence conservation between cattle and buffalo**.

### Next Step

Perform whole Y chromosome alignment between cattle and buffalo Y chromosome segments for further comparative genomic analysis.

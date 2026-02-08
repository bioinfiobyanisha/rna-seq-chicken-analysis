import pandas as pd
from collections import Counter

def load_gtf(gtf_file):
    genes = []
    with open(gtf_file) as f:
        for line in f:
            if line.startswith("#"):
                continue
            cols = line.strip().split("\t")
            if cols[2] == "gene":
                info = cols[8]
                gene_id = info.split("gene_id")[1].split(";")[0].replace('"', '').strip()
                genes.append(gene_id)
    return set(genes)

# Example GTF files (replace with your paths)
gtf_files = {
    "Goat_1": "data/goat1.gtf",
    "Goat_2": "data/goat2.gtf",
    "Goat_3": "data/goat3.gtf"
}

gene_sets = {k: load_gtf(v) for k, v in gtf_files.items()}

# Total gene count
gene_counts = {k: len(v) for k, v in gene_sets.items()}

# Common genes
common_genes = set.intersection(*gene_sets.values())

# Species-specific genes
specific_genes = {
    k: v - common_genes for k, v in gene_sets.items()
}

# Save results
df_counts = pd.DataFrame.from_dict(gene_counts, orient="index", columns=["Total_Genes"])
df_counts.to_excel("results/gene_counts.xlsx")

pd.DataFrame({"Common_Genes": list(common_genes)}).to_excel("results/common_genes.xlsx", index=False)

print("Analysis completed successfully")

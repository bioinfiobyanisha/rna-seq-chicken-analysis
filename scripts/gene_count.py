import pandas as pd
from pathlib import Path

# -------- FUNCTION TO EXTRACT GENES --------
def extract_genes(gtf_file):
    genes = set()

    with open(gtf_file, "r") as f:
        for line in f:
            if line.startswith("#"):
                continue

            fields = line.strip().split("\t")

            if len(fields) < 9:
                continue

            feature = fields[2]

            if feature == "gene":
                attributes = fields[8]

                for attr in attributes.split(";"):
                    if "gene_id" in attr:
                        gene_id = attr.split('"')[1]
                        genes.add(gene_id)

    return genes


# -------- INPUT FILES --------
gtf_files = {
    "Chicken": "data/chicken.gtf",
    "Sheep": "data/sheep.gtf",
    "Goat": "data/goat.gtf",
    "Pig": "data/pig.gtf"
}

gene_sets = {}
gene_counts = {}

# -------- CREATE OUTPUT FOLDER --------
Path("results").mkdir(exist_ok=True)

# -------- EXTRACT GENES --------
for species, gtf in gtf_files.items():

    print(f"Processing {species}...")

    genes = extract_genes(gtf)

    gene_sets[species] = genes
    gene_counts[species] = len(genes)


# -------- TOTAL GENE COUNT --------
gene_count_df = pd.DataFrame.from_dict(
    gene_counts,
    orient="index",
    columns=["Total_Genes"]
)

gene_count_df.to_excel("results/gene_counts.xlsx")


# -------- COMMON GENES --------
common_genes = set.intersection(*gene_sets.values())

pd.DataFrame({
    "Common_Genes": list(common_genes)
}).to_excel(
    "results/common_genes.xlsx",
    index=False
)


# -------- SPECIES SPECIFIC GENES --------
specific_genes = {}

for species in gene_sets:

    other_species = set.union(
        *(gene_sets[s] for s in gene_sets if s != species)
    )

    specific = gene_sets[species] - other_species

    specific_genes[species] = list(specific)


with pd.ExcelWriter("results/species_specific_genes.xlsx") as writer:

    for species, genes in specific_genes.items():

        df = pd.DataFrame({
            f"{species}_Specific_Genes": genes
        })

        df.to_excel(
            writer,
            sheet_name=species,
            index=False
        )


print("✅ Gene analysis completed successfully")

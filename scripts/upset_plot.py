import matplotlib.pyplot as plt
from upsetplot import UpSet, from_contents
from pathlib import Path


# ---------- FUNCTION TO EXTRACT GENES ----------
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


# ---------- INPUT FILES ----------
gtf_files = {
    "Chicken": "data/chicken.gtf",
    "Sheep": "data/sheep.gtf",
    "Goat": "data/goat.gtf",
    "Pig": "data/pig.gtf"
}


# ---------- CREATE OUTPUT FOLDER ----------
Path("results").mkdir(exist_ok=True)


# ---------- EXTRACT GENE SETS ----------
gene_data = {}

for species, gtf in gtf_files.items():

    print(f"Processing {species}...")

    gene_data[species] = extract_genes(gtf)


# ---------- PREPARE UPSET DATA ----------
upset_data = from_contents(gene_data)


# ---------- PLOT ----------
plt.figure(figsize=(10, 6))

upset = UpSet(
    upset_data,
    show_counts=True,
    sort_by="cardinality"
)

upset.plot()

plt.suptitle("Gene Overlap Across Livestock Species")

plt.savefig(
    "results/upset_plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


print("📊 UpSet plot generated successfully")

# Day 2 morning + lunch exercise 

## Biological Learning Objectives
- Summarize gene metadata retreived from BioMart
- Explore the GENCODE genome annotation
- Computational Learning Objectives
- Practice working at the command line
- Explore text files using core Unix programs


## Instructions: Complete the following exercises using a combination of cut, sort, uniq, and grep. Document each command you use, along with any short answers, in a single README.md file stored in ~/qbb2024-answers day2-lunch. Use Markdown headings, lists, and code blocks to organize your answers into sections and format content for proper display e.g.

## Example answer 1
- `wc -l hg38-gene-metadata-feature.tsv` 
- There are 61633 lines

# Exercises 

### BioMart provides a way to obtain genome annotation information (referred to as Attributes) such as gene IDs, transcripts, phenotypes, GO terms, structures, orthologues, variants, and more. This information can be retrieved through the web-based tool as well as the Bioconductor biomaRt package.

### Question 1. 
##### Tally the number of each gene_biotype in hg38-gene-metadata-feature.tsv. How many protein_coding genes are there? Pick one biotype you would want to learn more about and explain why.

Used this code to see which column within the file is for 'gene_biotype'
- head -n 1 hg38-gene-metadata-feature.tsv

Based on this output, I saw that 'gene_biotype' is the 7th column
- ensembl_gene_id	external_gene_name	chromosome_name	start_position	end_position	strand	gene_biotype	description 

Used this code to cut + sort for unique the different IG genes and tally them by their respective categories 
- cut -f7 hg38-gene-metadata-feature.tsv | sort | uniq -c 

This is the tally output of each 'gene_biotype' in the file 
- 10 IG_C_gene
- 4 IG_C_pseudogene
- 37 IG_D_gene
- 11 IG_J_gene
- 3 IG_J_pseudogene
- 108 IG_V_gene
- 144 IG_V_pseudogene
- 1 IG_pseudogene
- 2 Mt_rRNA
- 22 Mt_tRNA
- 1042 TEC
- 6 TR_C_gene
- 5 TR_D_gene
- 79 TR_J_gene
- 4 TR_J_pseudogene
- 107 TR_V_gene
- 33 TR_V_pseudogene
- 19 artifact
- 18804 lncRNA
- 1833 miRNA
- 2146 misc_RNA
- 9987 processed_pseudogene
- 19618 protein_coding
- 46 rRNA
- 92 rRNA_pseudogene
- 8 ribozyme
- 5 sRNA
- 1 scRNA
- 46 scaRNA
- 1875 snRNA
- 931 snoRNA
- 505 transcribed_processed_pseudogene
- 154 transcribed_unitary_pseudogene
- 918 transcribed_unprocessed_pseudogene
- 2 translated_processed_pseudogene
- 95 unitary_pseudogene
- 2525 unprocessed_pseudogene
- 4 vault_RNA

There are 19,618 protein coding genes. I would want to learn more about snoRNA because I have never read/learned about these before. Based on a quick literature search I did, it seems that this class of RNA helps stabilize the structure of rRNA through methylation. I would like to read more literature on how this methylation is done.

### Question 2. 

#### Which ensembl_gene_id in hg38-gene-metadata-go.tsv has the most go_ids? Create a new file that only contains rows corresponding to that gene_id, sorting the rows according to the name_1006 column. Describe what you think this gene does based on the GO terms.

 1. ENSG000XYZ  GO:0090425  acinar cell differentiation
 2. ENSG000XYZ  GO:0016323  basolateral plasma membrane
 3. ENSG000XYZ  GO:0045296  cadherin binding


Used this code to cut out the first column in the file and uniquely sorted to see the gene that has the most GO ID's.
- cut -f1 hg38-gene-metadata-go.tsv | uniq -c | sort -n

Based on the output, the gene 'ENSG00000168036' has the most with 273 go terms. 

Used this code to grab the rows with the gene 'ENSG00000168036' and sort them according to the third column 'name_1006'
- grep -w "ENSG00000168036" hg38-gene-metadata-go.tsv | sort -k3 > ENSG00000168036.txt

Based on the GO-terms I saw, it seems that this gene has a quite diverse role, mainly for transcription regulation (by interacting with DNA), signal transduction (MAPK cascade pathway, cell to cell adhesion), and developmental processes (cell differentiation (T-cells), cell fate/morphogenesis). 


### Question 3. GENCODE works to annotate the human and mouse genome using biological evidence such as long-read RNA-seq, Ribo-seq, and other targeted approaches. This gene set is used by many projects including Genotype-Tissue Expression (GTEx), The Cancer Genome Atlas (TCGA), and the Human Cell Atlas (HCA). Complete the following exercises using the gene.gtf that we created together

#### Question 3A. Immunoglobin (Ig) genes are present in over 200 copies throughout the human genome. How many IG genes (not pseudogenes) are present on each chromosome? You can use a dot (.) in a regular expression pattern to match any single character. How does this compare with the distribution of IG pseudogenes?

Used this code to grab the total IG genes for each unique chromosome by cutting it out and then printing the result. 
- grep -w "IG_._gene\|IG_.._gene" genes.gtf | cut -f1 | uniq -c | less -S
- grep -w "IG_._pseudogene" genes.gtf | cut -f1 | uniq -c | less -S

The output I received is for IG genes: 
- 52 chr2
- 91 chr14
- 16 chr15
- 6 chr16
- 1 chr21
- 48 chr22

vs IG pseudogenes
- 1 chr1
- 45 chr2
- 1 chr8
- 5 chr9
- 1 chr10
- 83 chr14
- 6 chr15
- 8 chr16
- 1 chr18
- 48 chr22

It seems that the IG pseudogenes are much more spread out and are clustered at 3 locations (chromosome 2, 14, and 22). In comparison, IG genes are at fewer locations in the later numbered chromosomes (starting from 14) and also seem to be clustered around 3 (chromosome 2, 14, and 22). It's interesting but logical that the pseudogenes and IG cluster at the same chrosome loci. 

#### Question 3B. Why is grep pseudogene gene.gtf not an effective way to identify lines where the gene_type key-value pair is a pseudogene (hint: look for overlaps_pseudogene)? What would be a better pattern? Describe it in words if you are having trouble with the regular expression.

When I ran 'grep pseudogene genes.gtf | less -S' to see what happens, I saw that variations of pseudogene was also seen in the 'tag' column, which means we aren't identifying lines in gene_type specifically for pseudogene but rather any line in any column that has pseudogene in it. 

A better pattern to use could be:
- grep 'gene_type ".*pseudogene"' genes.gtf | less -S

#### Question 3C. Convert the annotation from .gtf format to .bed format. Specifically, print out just the chromosome, start, stop, and gene_name. As cut splits lines into fields based on the tab character, first use sed to create a new file where spaces are replaced with tabs.

 - sed "s/ /\t/g" gene.gtf > gene-tabs.gtf
 - head -n1 genes_tabs.gtf
 - cut -f1,4,5,11 genes_tabs.gtf > genes_converted.txt | less -S

 First 5 outputs of 'genes_converted.txt'
1. chr1	11869	14409	"DDX11L2";
2. chr1	12010	13670	"DDX11L1";
3. chr1	14696	24886	"WASH7P";
4. chr1	17369	17436	"MIR6859-1";
5. chr1	29554	31109	"MIR1302-2HG";
 


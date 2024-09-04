# Day 2 morning, lunch exercise 

## Biological Learning Objectives
    #Summarize gene metadata retreived from BioMart
    #Explore the GENCODE genome annotation
    #Computational Learning Objectives

    #Practice working at the command line
    #Explore text files using core Unix programs


## Instructions: Complete the following exercises using a combination of cut, sort, uniq, and grep. Document each command you use, along with any short answers, in a single README.md file stored in ~/qbb2024-answers day2-lunch. Use Markdown headings, lists, and code blocks to organize your answers into sections and format content for proper display e.g.

## Example answer 1
- `wc -l hg38-gene-metadata-feature.tsv` 
- There are 61633 lines

## Exercises 

### BioMart provides a way to obtain genome annotation information (referred to as Attributes) such as gene IDs, transcripts, phenotypes, GO terms, structures, orthologues, variants, and more. This information can be retrieved through the web-based tool as well as the Bioconductor biomaRt package.

### Question 1. 
##### Tally the number of each gene_biotype in hg38-gene-metadata-feature.tsv. How many protein_coding genes are there? Pick one biotype you would want to learn more about and explain why.

##### Seeing which column within the file is for 'gene_biotype'
- head -n 1 hg38-gene-metadata-feature.tsv

#####  Based on this output, 'gene_biotype' is the 7th column
- ensembl_gene_id	external_gene_name	chromosome_name	start_position	end_position	strand	gene_biotype	description 

##### 
- cut -f7 hg38-gene-metadata-feature.tsv | sort | uniq -c 

##### Tally output of each 'gene_biotype' in the file 
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


### Question 2. 

#### Which ensembl_gene_id in hg38-gene-metadata-go.tsv has the most go_ids? Create a new file that only contains rows corresponding to that gene_id, sorting the rows according to the name_1006 column. Describe what you think this gene does based on the GO terms.

 1. ENSG000XYZ  GO:0090425  acinar cell differentiation
 2. ENSG000XYZ  GO:0016323  basolateral plasma membrane
 3. ENSG000XYZ  GO:0045296  cadherin binding

##### 

- cut -f1 hg38-gene-metadata-go.tsv | uniq -c | sort -n

#####
- 273 ENSG00000168036

- grep -w "ENSG00000168036" hg38-gene-metadata-go.tsv | sort -k3 > ENSG00000168036.txt

### Question 3. GENCODE works to annotate the human and mouse genome using biological evidence such as long-read RNA-seq, Ribo-seq, and other targeted approaches. This gene set is used by many projects including Genotype-Tissue Expression (GTEx), The Cancer Genome Atlas (TCGA), and the Human Cell Atlas (HCA). Complete the following exercises using the gene.gtf that we created together

#### Question 3A. Immunoglobin (Ig) genes are present in over 200 copies throughout the human genome. How many IG genes (not pseudogenes) are present on each chromosome? You can use a dot (.) in a regular expression pattern to match any single character. How does this compare with the distribution of IG pseudogenes?

total ig genes for each chromosome -> my interpretation so far 

grep -w "IG_._gene\|IG_.._gene" genes.gtf | cut -f1 | uniq -c | less -S


 52 chr2
  91 chr14
  16 chr15
   6 chr16
   1 chr21
  48 chr22

#### Question 3B. Why is grep pseudogene gene.gtf not an effective way to identify lines where the gene_type key-value pair is a pseudogene (hint: look for overlaps_pseudogene)? What would be a better pattern? Describe it in words if you are having trouble with the regular expression.



#### Question 3C. Convert the annotation from .gtf format to .bed format. Specifically, print out just the chromosome, start, stop, and gene_name. As cut splits lines into fields based on the tab character, first use sed to create a new file where spaces are replaced with tabs.

 sed "s/ /\t/g" gene.gtf > gene-tabs.gtf

Just for fun
A. Explore the GENCODE mouse annotation noting similaries and differences with the human annotation

"gene_type .*_pseudogene\";" (\ = escaping for grep)
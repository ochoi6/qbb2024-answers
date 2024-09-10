#!/usr/bin/env python3

#Using dictionaries to pull specific samples from GTEx data

#For this assignment, you will be looking at how much tissue expression varies across individuals for each of the highly expressed and tissue specific genes. To do this, you will be using the gene-tissue pair results from the morning advanced excercise (which is provided) to pull individual sample expression values for each of these gene-tissue pairs. You will also need the complete GTEx expression data file GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct and the sample attribute file GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt.
#For a description of GTEx, see the GTEx Portal.

#Because the expression data file is so large, you should create a smaller file to test and debug your script on. You can do this using the command:
#head -n 500 GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct > test_data.gct

##QUESTION 1. 
#Load the gene-tissue pairs from gene_tissue.tsv file (which are the 33 genes from the afternoon exercise yesterday)
#Create a dictionary keyed by the geneID with tissue as the value 

#Load libraries 
import sys

import numpy

#Save and open the files 
filename = sys.argv[1]
fs = open(filename, mode = 'r')
relevant_samples = {}

#For loop
for line in fs: 
    fields = line.rstrip("\n").split("\t") #strip off the new line and the tab separtion in file
    key = (fields[0]) #, fields[2]) #need an immutable key for our dictionary 
    relevant_samples[key] = fields[2] #relevant_samples[key] = [] #creating list for keys to hold the relevant samples

fs.close()

#print(relevant_samples)


##QUESTION 2. 
#Figure out which tissue corresponds to which sampleIDs
#Interested in SAMPID and SMTSD (specific tissue label)
#Create a dictionary using the tissue as the key
#Need the dictionary value to be a list that appends sample IDs using setdault
#To skip lines, first open using fs = open(fname) and then readline


#Save and open the file for metadata + want columns 0 and 6
filename = sys.argv[2]
fs = open(filename, mode = 'r')

#Skip the first line containing header
fs.readline()

#Create dict that holds samples for tussye name
tissue_samples = {}

#For loop
for line in fs: 
    fields = line.rstrip("\n").split("\t") #strip off the new line and the tab separtion in file
    #Create key from gene and tissue 
    key = (fields[6])
    value = (fields[0]) 
    tissue_samples.setdefault(key,[])
    tissue_samples[key].append(value) #creating list for keys to hold the relevant samples

fs.close()

#print(tissue_samples)

##QUESTION 3, 4, 5
#Need to get list of sampIDs in the tpm file 
#Load sampIDs that correspond to GTEx expression data file into a list 
#Row 2 and column 2

#Save and open the file for metadata + want columns 0 and 6
filename = sys.argv[3]
fs = open(filename, mode = 'r')

#Skip the first line containing header
fs.readline()
fs.readline()
header = fs.readline().rstrip("\n").split("\t")
header = header[2:]

#print(header)

tissue_columns = {}

for tissue, samples in tissue_samples.items():
    tissue_columns.setdefault(tissue, [])
    for sample in samples:
        if sample in header:
            position = header.index(sample)
            tissue_columns[tissue].append(position)

fs.close()

#print(tissue_columns)

#find number of samples per tissue_type -> ones with non-zero relevant expression data 

for tissue, columns in tissue_columns.items():
    print(tissue, columns) #Amount per tissue 
    print(len(columns))


##QUESTION 6. Now that you know which columns you need for any given tissue, you can load the expression file, keeping only genes that appear in the gene-tissue pair file and only epxression values from sampleIDs that correspond to the tissue of interest for that gene.
#To check if the gene is from the gene-tissue pair file, you can use the keyword in to see if a value is in the step 1 dictionary’s keys just like a list.
#If the gene is in the gene-tissue pair set, determine which tissue that gene is associated with, get the column indices for that tissue, and pull out only the expression values for the corresponding tissue.
#Unlike lists, numpy arrays can use a list of indices to pull out multiple values at the same time and much faster. With this in mind, when you find a target gene you should convert its expression values into a numpy array and then you can use the index list that you made step 5 to extract the tissue-specific expression values in one step.
#You will potentially have different numbers of expression values for each gene, so saving your data in a numpy array doesn’t make sense. Instead, you can use a couple of different approaches. A list with the geneID, tissue, and expressions is one option. A dictionary keyed by the geneID and tissue name with the expression value array as the coresponding value is another.


f = open("test_data.gct", "r")

for l in f:
    l = l.strip().split("\t")
    #print(l[0])

    geneName = l[0]
    #print(geneName)

    if geneName in relevant_samples.keys():
        myTissues = relevant_samples[geneName]
        print(tissue_columns[myTissues])





##QUESTION 7. Now that you have the relevant expression values, you need to save the results in a tab-separated file with one line per expression value, its corresponding geneID, and tissue.
#Your output should have 3 columns. You can do this using a nested for loop. The outer for loop looks at each gene while the inned for loop reads each expression value for that gene.

##QUESTION 8. Finally, you can visualize how variable each gene’s expression is.
#Load the data into R and create a violin plot of expression levels broken down by gene (ggplot2’s geom_violin()).
#For categories, create a combination of tissue names and gene IDs (dplyr::mutate(Tissue_Gene=paste0(Tissue, " ", GeneID)))
#You will need to log-transform your data with a psuedo-count of one (you can use dplyr::mutate for this step as well)
#Switch the axes for the violin plot so the categories are on the y-axis (coord_flip())
#Make sure to label your axes

#Given the tissue specificity and high expression level of these genes, are you surprised by the results?
#What tissue-specific differences do you see in expression variability? Speculate on why certain tissues show low variability while others show much higher expression variability.
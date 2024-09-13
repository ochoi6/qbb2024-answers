#!/usr/bin/env python3

# DAY 4 MORNING EXERCISE 

### Using dictionaries to pull specific samples from GTEx data

# For this assignment, you will be looking at how much tissue expression varies across individuals for each of the highly expressed and tissue specific genes. To do this, you will be using the gene-tissue pair results from the morning advanced excercise (which is provided) to pull individual sample expression values for each of these gene-tissue pairs. You will also need the complete GTEx expression data file GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct and the sample attribute file GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt.
# For a description of GTEx, see the GTEx Portal.

# Because the expression data file is so large, you should create a smaller file to test and debug your script on. You can do this using the command:
# head -n 500 GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct > test_data.gct

## QUESTION 1. 
# Load the gene-tissue pairs from gene_tissue.tsv file (which are the 33 genes from the afternoon exercise on day3 that we did in python dictionaries)
# Create a dictionary keyed by the geneID with tissue as the value 

# Load libraries 
import sys

import numpy

# Save and open the files 
filename = sys.argv[1]
fs = open(filename, mode = 'r')
relevant_samples = {}

# For loop to create a dictionary with key = geneID, value = tissue
for line in fs: 
    fields = line.rstrip("\n").split("\t") # Strip off the new line and the tab separtion in file
    key = (fields[2]) # Need an immutable key for our dictionary 
    relevant_samples[key] = fields[2] # Relevant_samples[key] = [] #creating list for keys to hold the relevant samples

# Close the file 
fs.close()

#print(relevant_samples)



## QUESTION 2. 
# File to use for sys.argv[2] = GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
# Figure out which tissue corresponds to which sampleIDs
# Interested in SAMPID and SMTSD (specific tissue label)
# Create a dictionary using the tissue as the key
# Need the dictionary value to be a list that appends sample IDs using setdault
# To skip lines, first open using fs = open(fname) and then readline

# Save, open, and read the metadata file 
filename = sys.argv[2]
fs = open(filename, mode = 'r')

# Skip the first line containing the header
fs.readline()

# Create a dictionary that holds samples for tissue names
tissue_samples = {}

# For loop
for line in fs: 
    fields = line.rstrip("\n").split("\t") # Strip off the new line and the tab separtion in file
    key = (fields[6]) #Creating the keys and values based on the 1st and 6th column of the file 
    value = (fields[0]) 
    tissue_samples.setdefault(key,[])
    tissue_samples[key].append(value) # Creating list for keys to hold the relevant samples

# Close the file 
fs.close() 

#print(tissue_samples)



## QUESTION 3, 4, 5, 6

# QUESTION 3: 
# Need to get the list of sampleIDs present in GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct
# Load the sample IDs corresponding to the expression data file into a list 

# Save, open, and read the file 
filename = sys.argv[3]
fs = open(filename, mode = 'r')

# Skip the first two lines because they simply contain header information
fs.readline()
fs.readline()

# Read the 3rd line for column headers, strip off the new line and split it by tabs 
header = fs.readline().rstrip("\n").split("\t")
header = header[2:] # Saying that I want to skip the first 2 lines 

#print(header)


# QUESTION 4:
# Create a dictionary keyed by each sampleID from question 3 with the column index as its value 

# Created a dictionary called tissue_columns and will define it in question 5 answer 
tissue_columns = {}


# QUESTION 5A:
# Create a new dictionary keyed by each tissue name with the value being a list of column indexes 
# Use a nested for loop to step through the tissue names followed by stepping through sampleIDs associated with that tissue 
# Check if each sampleID is present and if yes, add the column index to the correct tissue list in the new dictionary 

# For loop 
# Iterate over each tissue type and its associated sample IDs from the tissue_samples dictionary
for tissue, samples in tissue_samples.items():
    
    # Check that dictionary tissue_columns has an entry for the respective tissue -> if no, create an empty list for it correspondingly 
    tissue_columns.setdefault(tissue, [])
    
    # Iterate over each sampleID in the full list of sample IDs present for its corresponding respective tissue
    for sample in samples:
        
        # If the current sample ID exists in the header
        if sample in header:
            
            # Find the column index of the current sampleID in the header list
            position = header.index(sample)
            
            # Add (append) this column index to the full list of column indexes for the current tissue in the tissue_columns dictionary
            tissue_columns[tissue].append(position)

# Close the file 
fs.close()

#print(tissue_columns)


# For each tissue type, see how many samples have expression data

# For loop 

# Iterate for each tissue type and column (the key, value pair) in the tissue_columns dictionary 
for tissue, columns in tissue_columns.items():

    # Print the current 'tissue' and the corresponding 'columns'
    #print(tissue, columns) 

    # Print the length of 'columns' to see the number of sampleIDs present for each 
    print(len(columns))

# QUESTION 5B:
# Which tissue types have the largest number of samples? The fewest?

    # ANSWER: 
    #   Whole blood has the largest number of samples with a count of 755. 
    #   Cells - Leukemia cell line (CML) has the least number of samples with a count of 0. 
    #   If we were looking for a tissue type that did have samples but with the smallest count, it would be kidney - medulla with 4 samples. 

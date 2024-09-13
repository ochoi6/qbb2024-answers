#!/usr/bin/env python3

### USING NUMPY MATRICES AND INDEXING TO FIND MARKER GENES IN GTEX DATA

## Directions : 
# For a description of GTEx, see the GTEx Portal.
# Certain genes have high tissue specificity while some tissues are highly enriched in certain proteins. 
# In this assignment, you will be find the intersection between these two, identifying genes with a ten-fold enrichment in a single tissue and that are the highest expressed gene in their enriched tissue. To do this, you will be using a summary dataset that has the median expression levels across samples for each gene and tissue, named GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct.
# Please submit your answers as a .py script with comments explaining the logic of each code block and for questions regarding interpretation or discussion of your results, please include your answers as comments interspersed with your code or a separate text file (Remember that comment lines start with # and are ignored by Python and R). For advanced exercises, please also include the .tsv file with gene-tissue pairs.


# File to use: GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct


## Question 1. Load expression data into a nested list, the tissue names into a list, the gene IDs into a list, and the gene names into a list. 

# Steps to answering:
    # A. Open GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct file 
    # B. Based on the file format, skip the first 2 header lines 
    # C. Split column header and skip the first 2 header lines 
    # D. Find a way to hold genes names, gene IDs, and expression values
    # E. For each line: split it, save field 0 = gene names + field 1 = gene IDs + field 2 = expression values 


# In terminal, unzipped the metadata tpm file and viewed its format using these 2 code lines: 

#gunzip GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct
#less -S GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct


# Loaded 'sys' and 'numpy' library into current python environemnt 
import sys 

import numpy 


# Open and read the file 
fs = open(sys.argv[1], mode = 'r')


# Skip the first 2 header lines 
fs.readline()
fs.readline()


# Split the column header by tabs and skip first two entries 
line = fs.readline()
fields = line.strip("\n").split("\t")
tissues = fields[2:]



# Find a way to hold genes names, gene IDs, and expression values by intializing 3 empty lists for each variable of interest 
gene_names = []
gene_IDs = []
expression = []


# For each line: split it, save field 0 as gene names + field 1 as gene IDs, field 2 as expression values using for loops and append them
for line in fs:
    fields = line.strip("\n").split("\t")
    gene_names.append(fields[0])
    gene_IDs.append(fields[1])
    expression.append(fields[2:])


# Close the file 
fs.close()



## Question 2. Converting the nested lists into numpy arrays becase the nested lists are clunky to use and difficult to work with 
   

# Use 'numpy.array' on the 2 lists plus tissues and convert them back into the original list name 
gene_names = numpy.array(gene_names)
gene_IDs = numpy.array(gene_IDs)
tissues = numpy.array(tissues)


# Use 'numpy.array' on expression and add arguement 'dtype = float' to properly convert them 
expression = numpy.array(expression, dtype = float) 


    # Why do you need to tell numpy what type of data the expression data is but not for the other data lists?
    # Answer: The expression data is still a string because we never converted it and thus it is necessary to manually convert them to floats using the argument. 



## Question 3. SKIP 



## Question 4. Calculate the same mean expression values for the first 10 genes using the built in numpy function and then print it. 

# Calculating the mean expression values for the first 10 genes (aka the first 10 rows) across tissues (each column) and then printing it 
expression_10 = numpy.mean(expression[0:10,:], axis = 1)
#print(expression_10)

    # Do they match the means you found with the nested for loop approach?
    # Answer: Skippped answering because we didn't do question 3. 



## Question 5. Calculate and compare the median, mean expression value of the entire dataset to get a sense of the spread of data and then print it. BUT don't use the axis argument. 

# Using the numpy commands for both median + mean on expression values and save it in its own variable 
expression_median_all = numpy.median(expression)
expression_mean_all = numpy.mean(expression)

#print(expression_median_all) #expression_median_all = 0.0271075
#print(expression_mean_all)   #expression_mean_all = 16.557814350910945

    # What can you infer from the difference between these statistics?
    # Answer: Based on our values, the mean value is much higher than the median. This suggests that there is a probability of extreme outliers in the dataset affecting the discrepancy and causing the mean to be pulled up. 



## Question 6. Apply a log-transformation to the data to work with a more normalized range of expression values and check the median + mean values again. 

# Use a log2 transformation to keep the values interpretable and add a pseudo-count of 1 to avoid taking the log of zero
expression_pseudo = expression + 1 # Performing a pseudo-count by adding 1 to each expression value and saving it into 'expression_pseudo'
#print(expression_pseudo)

expression_log2 = numpy.log2(expression_pseudo) # Running log2 on the pseudo expression variable 
#print(expression_log2)

expression_median_log2_all = numpy.median(expression_log2) # Running median on the log2 pseudo-counted +1 expression variables 
expression_mean_log2_all = numpy.mean(expression_log2) # Running mean on the log2 pseudo-counted +1 expression variables 
print(expression_median_log2_all) #expression_median_log2_all = 0.03858718613570538
print(expression_mean_log2_all)   #expression_mean_log2_all = 1.1150342022364093

    # Now do the median and mean transformed expression values compare to each other? To the non-transformed values? 
    # Answer: The mean transformed expression value is still quite a bit larger than the median by ~37x increase. The transformed value is bigger than the non-transformed value for median (due to it simply beign a log transformation) and the transformed value is ~16x smaller than the non-transformed value for mean (probably because the non-transformed was super variable and performing the log decreases the variability/effect of extreme values)



## Question 7. Find the expression gap for each gene between their highest and 2nd highest expression level to identify highly specific genes 

# Sort the tissues by expression values and specify an axis. Save it into a new variable called 'expression2_log'
expression2_log = numpy.sort(expression_log2, axis = 1) 
#print(expression2_log)

# For each gene, find the difference between highest and second highest expression value. Did the backwards annotation value and took the last and second to last values (since sorting goes in ascending order)
highest_expression = expression2_log[:, -1]
second_highest_expression = expression2_log[:, -2]
diff_array = highest_expression - second_highest_expression

#print(diff_array)
#print(len(diff_array)) #length of diff_array = 56,200 genes (which checks out and confirms that this worked correctly)



##Question 8: Using the array just created, identify genes that show high single-tissue specficity as defined as a difference of at lease t10 (~1000 fold difference since the data is log2 transformed)

# Print the number of genes whose difference between the highest and second highest tissue expression is greater than 10
#print(numpy.sum(diff_array >= 10)) #The sum of genes that are greater than or equal to 10 = 33 genes 

#print("Values bigger than 10 =", diff_array[diff_array > 10])
#Values bigger than 10 = [10.78748239 10.67634364 10.67685089 10.79258601 10.63401346 10.03363193
#                         11.27907424 11.37211554 12.72612096 13.13515163 12.17289528 11.00234853
#                         12.0395889  11.38802103 10.96751173 12.22206229 10.57444814 10.33457191
#                         12.23385405 12.45561106 10.93647187 10.62483158 10.1475093  10.27852231
#                         10.35457175 10.50602358 12.29869899 12.34453924 11.78097106 11.95448632
#                         10.79513137 13.04897769 10.27816413]

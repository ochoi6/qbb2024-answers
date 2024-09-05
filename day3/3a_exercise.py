#!/usr/bin/env python3


##THINGS TO DO 
#open file
#skip 2 lines 
#split column header by tabs and skip first two entries 
#create way to hold gene names 
#create way to hold expression values 
#for each line: split line, save field 1 into gene names, save 2+ into expression values 

#gunzip GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct
#less -S GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct

#python -> can also make this executeable but have to write it each time 

import sys #internal built in library

import numpy #external library 

#open and read the file 
fs = open(sys.argv[1], mode = 'r')

#skip the 2 lines 
fs.readline()
fs.readline()

#split column header by tabs and skip first two entries 
line = fs.readline()
fields = line.strip("\n").split("\t")
tissues = fields[2:]

#create way to hold gene names 
#create way to hold gene IDs 
#create way to hold expression values 
gene_names = []
gene_IDs = []
expression = []


#for each line: split line, save field 0 into gene names, save field 1 into gene IDs, save 2+ into expression values 
for line in fs:
    fields = line.strip("\n").split("\t")
    gene_names.append(fields[0])
    gene_IDs.append(fields[1])
    expression.append(fields[2:])

fs.close()

tissues = numpy.array(tissues)
gene_IDs = numpy.array(gene_IDs)
gene_names = numpy.array(gene_names)
expression = numpy.array(expression, dtype = float) #still strings because we never converted them 

##question 4: numpy means of first 10 genes for expression 

expression_10 = numpy.mean(expression[0:10,:], axis = 1)
#print(expression_10)

##question 5: calculate and compare the median, mean expression value of the entire dataset -> don't use axis argument 

expression_median_all = numpy.median(expression)
expression_mean_all = numpy.mean(expression)

#print(expression_median_all)
#print(expression_mean_all)

##question 6: apply a log-transformation to the data and check the mean, median values again + because there are zeros so use a pseudo-count of one 

expression_pseudo = expression + 1
#print(expression_pseudo)

expression_log2 = numpy.log2(expression_pseudo)
#print(expression_log2)

expression_median_log2_all = numpy.median(expression_log2)
expression_mean_log2_all = numpy.mean(expression_log2)

#print(expression_median_log2_all)
#print(expression_mean_log2_all)

##question 7: find expression gap for each gene between highest and next highest expression level to identify highly tissue specific genes

#sort across tissues by expression values and specify an axis 
expression2_log = numpy.sort(expression_log2, axis = 1)
#print(expression2_log)


#for each gene, find the difference between highest and second highest expression value 
highest_expression = expression2_log[:, -1]
second_highest_expression = expression2_log[:, -2]


diff_array = highest_expression - second_highest_expression

#print(diff_array)
#print(len(diff_array))


##question 8: identify genes that show high single tissue specificity as defined as a difference of at least (~1000-fold difference since the data are log2-transformed)

#Print the number of genes whose difference between the highest and second highest tissue expression is greater than 10.

print("Values bigger than 10 =", diff_array[diff_array > 10])

print(numpy.sum(diff_array >= 10))


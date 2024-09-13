#!/usr/bin/env python3

#Question 2. (gtf2bed.py) Create a program that converts genome annotation information from .gtf format to .bed format. Specifically, print out just the chromosome, start, stop, and gene_name, stripping off both the beginning gene_name " and ending ".

#Load sys into the environment 
import sys

#Setting file as the second thing to consider in the command line to open it when running the loop
file = open(sys.argv[1])

#For loop
for line in file: 
    if "##" in line: #This is to skip the beginning parts of the file where there '##' and continue past to the actual content 
        continue
    fields = line.split("\t") #This is to say that each element/column is split by tab for every line
    chrom = fields[0] 
    start = fields[3]
    end = fields[4]
    fields2 = fields[8].split(";") #In the file, there is a sub-split where the right half of it is split by a semicolon and we created a new 'fields2' variable to store it 
    gene = fields2[2]
    print(chrom + "\t" + start + "\t" + end + "\t" + gene.lstrip("gene_name \"").rstrip("\"")) #Printing the result and stripping the "gene_name" + quotations


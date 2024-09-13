#!/usr/bin/env python3

#Question 1. (grep.py) Warm up by implementing a basic grep program to practice indexing the sys.argv list, processing a text file line-by-line, and removing the newline character.

#Load sys into the environment 
import sys

#Setting gene pattern (example = FIS1) as the second thing to consider and setting file as the third thing to consider in the command line to open it when running the loop
gene_pattern = sys.argv[1]
file = open(sys.argv[2])

#For loop to reiterate over every line in the file 'gencode.v46.basic.annotation.gtf'
for line in file:
    if gene_pattern in line: 
        print(line.rstrip("\n")) #This is to remove the newline character present in each line 
        
file.close()
    

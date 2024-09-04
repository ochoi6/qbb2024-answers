#!/usr/bin/env python3

#Question 2. (gtf2bed.py) Create a program that converts genome annotation information from .gtf format to .bed format. Specifically, print out just the chromosome, start, stop, and gene_name, stripping off both the beginning gene_name " and ending ".

#import the program needed 
import sys

#Specifically, print out just the chromosome, start, stop, and gene_name, stripping off both the beginning gene_name " and ending ".
file = open(sys.argv[1])

for line in file: 
    if "##" in line:
        continue
    fields = line.split("\t")
    chrom = fields[0]
    start = fields[3]
    end = fields[4]
    fields2 = fields[8].split(";")
    gene = fields2[2]
    print(chrom + "\t" + start + "\t" + end + "\t" + gene.lstrip("gene_name \"").rstrip("\""))


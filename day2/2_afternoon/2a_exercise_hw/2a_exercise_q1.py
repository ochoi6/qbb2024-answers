#!/usr/bin/env python3

#Question 1. (grep.py) Warm up by implementing a basic grep program to practice indexing the sys.argv list, processing a text file line-by-line, and removing the newline character.

#import the program needed 
import sys

gene_pattern = sys.argv[1]
file = open(sys.argv[2])

for line in file:
    if gene_pattern in line:
        print(line.rstrip("\n"))

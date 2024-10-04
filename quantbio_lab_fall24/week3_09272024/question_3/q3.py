#!/usr/bin/env python3

import sys 
import numpy 

allele_frequencies = []
print(allele_frequencies)


# step 3.1 

for line in open('biallelic.vcf'):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')

    # creating a column for information fields 
    info_field = fields[7]
    
    # splitting the information fields column 7 into the key-value pairs and separating the two with a semicolon 
    info_parts = info_field.split(';')
    
    # creating an empty variable to store allelic frequency values 
    af_value = None
    
    # nested for loop that looks for values within info_parts that contain anything with AF in it 
    for part in info_parts:
        if part.startswith('AF='):
            # taking that af value and because we want anything after the equal sign using part split and saving it into af_value
            af_value = part.split('=')[1]
            break
    
    # If AF value is found convert it to a float and using append function to add it to the af_value 
    if af_value is not None:
        allele_frequencies.append(float(af_value))

# opening a file called AF.txt 
with open('AF.txt', 'w') as af_file:
    # writing the header for it as 'Allele Frequency' and adding new line 
    af_file.write("Allele_Frequency\n")
    
    # writing each new allele frequency value and creating a new line after it 
    for af in allele_frequencies:
        af_file.write(f"{af}\n")

# printing out the list of allele frequencies to check the values and see if it worked 
print("Extracted Allele Frequencies:", allele_frequencies)


# step 3.2 

# extract the read depth of each variant site in each sample and output to DP.txt
# plot a histogram showing distribution of read depth at each variant across all samples - set bins = 21 and xlim(0,20)


# grep "^#" biallelic.vcf
##CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	A01_62	A01_39	A01_63	A01_35	A01_31	A01_27	A01_24	A01_23	A01_11	A01_09
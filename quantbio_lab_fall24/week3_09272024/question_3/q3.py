#!/usr/bin/env python3

#### < EXERCISE 3: : VARIANT DISCOVERY AND GENOTYPING + EXPLORATORY DATA ANALYSIS >

# Instructions: Obtain file from dropbox 

### STEP 3.1: Parse VCF file 


### STEP 3.2: Allele frequency spectrum 

## Instructions: 
    # Extract allele frequency of each variant and output it to a new file called AF.txt
    # Can be extracted from the variant specific INFO field 
    # Plot a histogram in R showing the allele frequency spectrum of the variants in VCF and set bins = 11 to avoid binning artifacts



## QUESTION 3.1: Interpret this figure in two or three sentences in your own words. Does it look as expected? Why or why not? Bonus: what is the name of this distribution?

    # ANSWER FOR 3.1: Yes, the figure looks as expected because it shows that there are variants in our data but the overall distribution of it is on the lower side since having many new mutations is rarer. Additionally, the figure displays a normal bell curve distribution. 



### STEP 3.3: Read depth distribution 

## Instructions: 
    # Extract read depth of each variant site in each sample and output it to a new field called DP.txt
    # Can be extracted from the sample specific FORMAT fields and the end of each line 
    # Plot a histogram showing distribution of read depth at each variant across all samples and set bins = 21, xlim = 0 to 20 to make the figure more legible 


## QUESTION 3.2: Interpret this figure in two or three sentences in your own words. Does it look as expected? Why or why not? Bonus: what is the name of this distribution?

    # ANSWER FOR 3.2: If this is the vcf that is connected to the sequencing coverage I caluclated for question 1, it makes sense because I calculated there is around 4x coverage for the reads. We can see that the general trend is the read depth is between the 4 and 5 range. The distribution is positively skewed normal distribution.  



# Code for 3.1: Importing the sys and numpy packages into my current python environment 
import sys 
import numpy 


# Code for 3.2: creating an empty variable list called 'allele_frequencies' to store the extracted values and printing it to check that it worked
allele_frequencies = []
print(allele_frequencies)


# Code for 3.3: creating an empty variable list called 'read_depths' to store the extracted values and printing it to check that it worked
read_depths = []
print(read_depths)


# Code for 3.1: using the given for-loop python script to parse the 'biallelic.vcf' downloaded from Dropbox
for line in open('biallelic.vcf'):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')

    # Code for 3.2: extracting the 7th (technically 8 but python starts from 0) field and saving it into the variable called 'info_field'
    info_field = fields[7]
    
    # Code for 3.2: splitting the information fields extracted from column 7 using semicolons to get the individual key-value pairs using 'split' command
    info_parts = info_field.split(';')
    
    # Code for 3.2: creating an empty variable to temporarily hold the extracted AF values  
    af_value = None
    
    # Code for 3.2: using a nested for loop that loops through each key-value pair in 'info_parts' and looking for the key that is 'AF=' and splitting it to only get the value coming after the equal sign and I included break to ensure that once it is found there are no unnecessary repeats that may occur 
    for part in info_parts:
        if part.startswith('AF='):
            af_value = part.split('=')[1]
            break
    
    # Code for 3.2: using a conditional statement to say, if the AF value is found to convert it to a float (because it will be a string) and add it to the empty intial list called 'allele_frequencies' using append
    if af_value is not None:
        allele_frequencies.append(float(af_value))

    # Code for 3.3: extracting the 8th column from the FORMAT field (technically 9th but since its python and we start from 0) for read depths (DP) and saving it into 'format_field'
    format_field = fields[8]

    # Code for 3.3: taking the sample-specific field from the 9th column and onwards containing information for each sample and saving it into 'sample' variable 
    samples = fields[9:] 
    
    # Code for 3.3: splitting the information fields extracted from column 8 using colons to get the individual key-value pairs using 'split' command and saving it into 'format_keys'
    format_keys = format_field.split(':')

    # Code for 3.3: using a conditional if...else... statement to find the index of the read depth keys in the 'format_keys' and saving it to 'dp_index'
    dp_index = format_keys.index('DP') if 'DP' in format_keys else None
    
    # Code for 3.3: from the conditional statement above for dp_index, if it was found, I want to loop it over each sample-specific field from 'samples' variable and saving it in 'sample_values'
    if dp_index is not None:
        for sample in samples:
            sample_values = sample.split(':')
            
            # Code for 3.3: error-checking step by checking that the 'dp-index' actually exists in the sample's data and if yes, appending the results into the intially created 'read_depths' variable list 
            if dp_index < len(sample_values):
                dp_value = sample_values[dp_index]
                read_depths.append(dp_value)


# Code for 3.2: opening a file called AF.txt in writing mode ('w') 
with open('AF.txt', 'w') as af_file:
    # Code for 3.2: creating a header in the file called "Allele Frequency" and making a new line 
    af_file.write("Allele_Frequency\n")
    
    # Code for 3.2: writing each new allele frequency value saved in the list 'allele_frequencies' and creating a new line after it 
    for af in allele_frequencies:
        af_file.write(f"{af}\n")

# Code for 3.2: printing out the list of allele frequencies to check the values and see if it actually worked 
print("Extracted Allele Frequencies:", allele_frequencies)


# Code for 3.3: opening a file called DP.txt in writing mode ('w') 
with open('DP.txt', 'w') as dp_file:

    # Code for 3.3: creating a header in the file called "Read Depth" and making a new line 
    dp_file.write("Read_Depth\n")
    
    # Code for 3.2: writing each new read depth value saved in the list 'read_depths' and creating a new line after it 
    for dp in read_depths:
        dp_file.write(f"{dp}\n")

# Code for 3.3: printing out the list of read depths to check the values and see if it actually worked 
print("Extracted Read Depths:", read_depths)



#!/usr/bin/env bash

#### < EXERCISE 1 : Get to know your data > 

### Instructions : 
    # 1) Take a glance at the first file, A01_09.fastq. These are single-end whole-genome DNA sequencing data from an Illumina sequencer. 
    # 2) Use your knowledge of FASTQ files (see Mike Sauria’s previous lecture) and the UNIX commands you have learned from previous classes to answer the following questions:





### QUESTION 1.1
    # How long are the sequencing reads?

## CODE FOR 1.1 : 

# Printing 'A01_09.fastq' file to double check its format: each read has 4 lines (identifier, sequence, sign + identifier, and quality scores)
#head A01_09.fastq 
#@HWI-ST387_0114:5:47:16737:7355#0
#ACACCACACACCACACCACACCCACACACACACATCCTAACACTACCCTAACACAGCCCTAATCTAACCCTGGCCA
#+
#@FGDFGFGGDGGGGHHGHEHHHGHHHGFHHFFDC>DEEEEDDB<BE>?7?>C@@@@CDBDDF?E2FBDAA>361::
#@HWI-ST387_0114:5:42:14962:12601#0
#ACAGCACCCACACACACACATCCTAACACTACCCTAACACAGTCCTAATCTAACCCTGGCCAACCTGTCTCTCAAC
#+
###############BB>B@.CAAC<9;@61=A>/BADAD:E;FECDFCB=FCFGFAGFGG@DFGEFFFDEDGGGE
#@HWI-ST387_0114:5:23:10710:84112#0
#CACCCACACACACACATCCTAACACTACCCTAACACAGCCCTAATCTAACCCTGGCCAACCTGTCTCTCAACTTAC

# Creating a variable called 'read_length' to calculate the lenth 
read_length=$(head -n 2 ~/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_09.fastq | tail -n 1 | awk '{print length}')
    # head -n 2 ~/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_09.fastq -> taking the first 2 lines from the file
    # tail -n 1 -> from those 2 lines, the one of interest is the second one because it contains the sequence 
    # awk '{print length}' -> using 'awk' command to print the length of the sequence 

# Printing 'read_length' variable to see what the length of the sequnece is 
echo $read_length


## ANSWER FOR 1.1 :
    # The sequencing reads are 76 base pairs long. 





### QUESTION 1.2 
    # How many reads are present within the file?

## CODE FOR 1.2 : 

# Creating a variable called 'lines_in_file' to store the total of number of lines present in 'A01_09.fastq'
lines_in_file=$(wc -l < ~/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_09.fastq)
    # wc -l -> asking for word count of the number of lines in my file 
    # < -> removes printing the filename pathway from printing when giving me the output 
    # ~/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_09.fastq -> pathway to file of interest 

# Printing the variable 'lines_in_file' and based on its output, there are 2678192 total lines 
echo $lines_in_file

# Creating a variable called 'number_of_reads' to store the total number of reads in 'A01_09.fastq'
number_of_reads=$((lines_in_file / 4))
    # Because I know that for each read there are a total of 4 lines associated with it, I can divide the total number of lines by 4 to get the number of reads 
    # Using the variable 'lines_in_file' (which contains total number of lines in the file), I simply divide it by 4 

# Printing the variable 'number_of_reads' and based on its output, there are 669548 total reads 
echo $number_of_reads


## ANSWER FOR 1.2 : 
    # There are 669,548 reads present in this file 





### QUESTION 1.3
    # Given your answers to 1 and 2, as well as knowledge of the length of the S. cerevisiae reference genome, what is the expected average depth of coverage?

## CODE FOR 1.3 : 
# Yeast genome = ~ 0.1 GB 
# Reads = 669,548 
# Length of reads = 76 bp 

# genome_length = 12157105
genome_length=$(awk '/^>/ {next} {total += length($0)} END {print total}' ~/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/sacCer3.fa)
echo $genome_length

# coverage = 4 
coverage=$((read_length*number_of_reads/genome_length))
echo $coverage

## ANSWER FOR 1.3 : 4x coverage 

### QUESTION 1.4 
    # While you do not need to repeat for all samples, looking at the size of the files can give us information about whether we have similar amounts of data from other samples. 
    # Use the du command to check the file sizes of the rest of the samples. Which sample has the largest file size (and what is that file size, in megabytes)? 
    # Which sample has the smallest file size (and what is that file size, in megabytes)?



### QUESTION 1.5 
    # Run the program FastQC on your samples (with default settings). 
    # Open the HTML report for sample A01_09.
    # What is the median base quality along the read? 
    # How does this translate to the probability that a given base is an error? 
    # Do you observe much variation in quality with respect to the position in the read?

FastQC ~/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_*.fastq

# Median base quality = 35 
# base error is 10^-3.5 
# variation seems to increase towards the beginning and end of the read

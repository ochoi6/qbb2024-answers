#!/usr/bin/env bash

#### < EXERCISE 1 : Get to know your data > 

### Instructions : 
    # 1) Take a glance at the first file, A01_09.fastq. These are single-end whole-genome DNA sequencing data from an Illumina sequencer. 
    # 2) Use your knowledge of FASTQ files (see Mike Sauria’s previous lecture) and the UNIX commands you have learned from previous classes to answer the following questions:





### QUESTION 1.1
    # How long are the sequencing reads?

## ANSWER FOR 1.1 :
    # The sequencing reads are 76 base pairs long. 



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

# Printing 'read_length' variable to see what the length of the sequnece is (read_length = 76)
echo $read_length





### QUESTION 1.2 
    # How many reads are present within the file?

## ANSWER FOR 1.2 : 
    # There are 669,548 reads present in this file 

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





### QUESTION 1.3
    # Given your answers to 1 and 2, as well as knowledge of the length of the S. cerevisiae reference genome, what is the expected average depth of coverage?

## ANSWER FOR 1.3 : 4x coverage 

## CODE FOR 1.3 : 
# Yeast genome = ~ 0.1 GB (know this from Bob's lecture)
# Reads = 669,548 (know this from question 1.2)
# Length of reads = 76 bp (know this from question 1.1)

# Using 'awk' command to process the yeast genome file sacCer3.fa line by line
genome_length=$(awk '/^>/ {next} {total += length($0)} END {print total}' ~/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/sacCer3.fa)
    # Used ''/^>/ {next}' to skip any line that has a new header
    # '{total += length($0)}' to take each non-header line to calculate the length of the sequence and then add it to the cumulative total
    # 'END {print total}' to give me a total sum of the lengths of each non-header line in the genome file 
    # Saving the results of it into the variable called 'genome_length'

# Printing the variable 'genome_length' and gettung the result 12157105
echo $genome_length

# Calculating coverage based on Michael Schatz's lecture and saving it into the variable called 'coverage'
coverage=$((read_length*number_of_reads/genome_length))

# Printing the variable 'coverage' to getting the result ~4.18x 
echo $coverage





### QUESTION 1.4 
    # While you do not need to repeat for all samples, looking at the size of the files can give us information about whether we have similar amounts of data from other samples. 
    # Use the du command to check the file sizes of the rest of the samples. Which sample has the largest file size (and what is that file size, in megabytes)? 
    # Which sample has the smallest file size (and what is that file size, in megabytes)?

## ANSWER FOR 1.4 : Largest file size is A01_62.fastq at 149 MB and the smallest file size is A01_27.fastq at 110 MB. 

## CODE FOR 1.4 : 

# Using 'du' to compare file sizes 
du -sh ~/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/* | sort -h
    # Using the 'du' command as noted in the question with the '-sh' option to summarize the total size of each file using human readable metrics 
    # Included 'sort -h' to  sort the output of du by size from smallest to largest 

# Output of the du command used above 

#110M	/Users/cmdb/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_27.fastq
#111M	/Users/cmdb/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_31.fastq
#113M	/Users/cmdb/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_63.fastq
#119M	/Users/cmdb/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_11.fastq
#122M	/Users/cmdb/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_09.fastq
#129M	/Users/cmdb/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_23.fastq
#130M	/Users/cmdb/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_39.fastq
#145M	/Users/cmdb/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_24.fastq
#146M	/Users/cmdb/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_35.fastq
#149M	/Users/cmdb/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_62.fastq





### QUESTION 1.5 
    # Run the program FastQC on your samples (with default settings). 
    # Open the HTML report for sample A01_09.
    # What is the median base quality along the read? 
    # How does this translate to the probability that a given base is an error? 
    # Do you observe much variation in quality with respect to the position in the read?

## ANSWER FOR 1.5 : The median base quality along the read is around 35. This means that the probability that a given base is an error is 10^-3.5. Variation seems to increase towards the beginning and end of the read in terms of position, while it stabilizes into a plateau in the middle. 

# Running fastqc on all the fastq files 
FastQC ~/qbb2024-answers/quantbio_lab_fall24/week3_09272024/week3_data/A01_*.fastq



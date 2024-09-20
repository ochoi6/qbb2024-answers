#!/usr/bin/env python3

### EXERCISE 1 : COVERAGE SIMULATOR 

## < STEP 1.5 > 

## Instructions : 
    # 1) Simulate sequencing 10x coverage of a 1 Mb genome with 100 bp reads
    # 2) Randomly sample ppositions in the genome and record the coverage
    # 3) Start position of each read should have a uniform random probability at each possible starting position (0 to 999,900)
    # 4) Record the coverage in an array of 1M positions 
    # 5) Save coverages into a text file that can be opened in R for plotting


# Importing the necessary packages into the current python script environment 
import numpy

import scipy 

# Defining the genome size, read length, and coverage I want 
genome_size = 1000000 # 1 Mbp genome 
read_length = 100 # 100 bp reads 
coverage = 10 # 10x coverage 



# Print the saved variables to check that it is working 
#print(genome_size)
#print(read_length)
#print(coverage)



# Calculating the number of reads needed 
number_of_reads = int((coverage * genome_size) / read_length)

#print(number_of_reads) # -> number_of_reads = 100000




# Using an array to keep track of the coverage for each position of the genome
genome_coverage = numpy.zeros(genome_size, dtype = int)

#print(genome_coverage) # -> genome_coverage = [0 0 0 ... 0 0 0]




# Simulating the sequencing reads using a for loop 
for i in range(number_of_reads):
    start_position = numpy.random.randint(0, genome_size - read_length)
    end_position = start_position + read_length
    genome_coverage[start_position:end_position] += 1

print("Start position:", start_position) # Start position: 601227
print("End position:", end_position) # End position: 601327
print("Genome coverage:", genome_coverage) # Genome coverage: = [0 0 0 ... 0 0 0]


numpy.savetxt('q1_5_genome_coverage.txt', genome_coverage, fmt='%d')
#!/usr/bin/env python3

# Step 1.2

# The start position of each read should have a uniform random probabilty at each possible starting position (0 through 999,900). 
# You can record the coverage in an array of 1M positions.


import numpy

number_reads = calculate_number_of_reads(genomesize, readlength, coverage)

genome_coverage = intialize_array_with_zero(genomesize)

for i in range(len(number_reads)):
    start_pos = uniform_random(1, genome_length - read_length)
    end_pos = start_pos + read_length - 1
    for x in range(start_pos, end_pos):
        genome_coverage[x] = genome_coverage[x] + 1

max_coverage = max(genome_coverage)
xs = list(range(0, max_coverage+1))

poisson_estimates = get_poisson_estimates(xs, lambda = genome_coverage)


normal_estimates = get_normal_estimates(xs, mean = genome_coverage, stdev = sqrt(genome_coverage))



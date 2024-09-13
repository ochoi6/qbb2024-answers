#!/usr/bin/env python3

import numpy 

import scipy

chrom = numpy.zeros(1000000, int)
#print(chrom)

#print(numpy.random.rand())
#print(numpy.random.rand(10))

# uniform random number generator 

#print(numpy.random.randint(0, 10, size = 10))

#size of the read - 1 = to picka  read that picks the read that spans 

#print(numpy.random.randint(1, ))

# scientific pi = numpy's bestie 

print(scipy.stats.poisson)
print(scipy.stats.norm)

print(scipy.stats.norm.rvs())

#scipy.stats.norm.pdf(1)

print(scipy.stats.poisson.pmf(1, 1))
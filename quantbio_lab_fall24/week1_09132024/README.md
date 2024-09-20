# Week 1 exercises : Genome assembly 

## < Exercise 1 > 

### Step 1.1 

#### Instructions : In your README.md for this assignment, answer the following question (show your work): How many 100bp reads are needed to sequence a 1Mbp genome to 3x coverage?


ANSWER : 30,000 reads are needed to sequence 1 Mbp genome to 3x coverage using 100 bp reads. 

(1 Mb genome) x (3x coverage) = 3 Mbp of data needing to be sequenced 

3 Mbp / (100 bp/read) = 0.03 M reads 


### Step 1.3

#### Instructions : What do we need to do to transform these probabilities into a frequency count comparable to those in our histogram? 

ANSWER : I first need to calculate the total frequency of genome coverages from the histogram. Then, I need to scale the poission and normal distribution probabilities to my data (so by multiplying by N, which equals 1,000,000). 


### Step 1.4

#### Instructions : (1) In your simulation, how much of the genome has not been sequenced (has 0x coverage)? (2) How well does this match Poisson expectations? How well does the normal distribution fit the data?


ANSWER : (1) 49,240 sites had 0x coverage. (2) The poisson distribution seems to fit the data better than the normal distribution, which is to be expected because it has lower coverage. 

grep -w '0' q1_2_genome_coverage.txt | wc -l

- Using 'grep' command to grab for any '0' in the file 
- Using the options 'wc -l' to tell us to count the length of the number of '0' present 


### Step 1.5

#### Instructions : (1) In your simulation, how much of the genome has not been sequenced (has 0x coverage)? (2) How well does this match Poisson expectations? How well does the normal distribution fit the data?

ANSWER : (1) 61 sites had 0x coverage. (2) Both probability distributions fit a bit better than when it was 3x coverage, but normal distribution does fit the curve just a bit better. This is expected of poisson because it is better at modeling count data.  

grep -w '0' q1_5_genome_coverage.txt | wc -l
- Using 'grep' command to grab for any '0' in the file 
- Using the options 'wc -l' to tell us to count the length of the number of '0' present 


### Step 1.6

#### Instructions : (1) In your simulation, how much of the genome has not been sequenced (has 0x coverage)? (2) How well does this match Poisson expectations? How well does the normal distribution fit the data?

ANSWER : (1) 2 sites had 0x coverage. (2) Both normal and poisson distribution fit the coverage model very well. This is to be expected because we have relatively high coverage in general and so our distirbutions also reflect this trend. 

grep -w '0' q1_6_genome_coverage.txt | wc -l
- Using 'grep' command to grab for any '0' in the file 
- Using the options 'wc -l' to tell us to count the length of the number of '0' present 


## < Exercise 2 > 

### Step 2.4 

#### Instructions : Now, use dot to produce a directed graph. Record the command you used in your READMD.md. Upload this graph as ex2_digraph.png in your submission directory. You do NOT need to upload the text file of edges you used to make the graph.

COMMAND USED : 

dot -Tpng de_bruijn_graph_edges.dot > ex2_digraph.png


- input file = de_bruijn_graph_edges.dot
- output png file = ex2_digraph.png
- Tpng indicates that I want my output in PNG format 
- dot is a command tool from graphviz 


### Step 2.5 

#### Instructions :  Assume that the maximum number of occurrences of any 3-mer in the actual genome is five. Using your graph from Step 2.4, write one possible genome sequence that would produce these reads. Record your answer in your README.md.

ANSWER : Based on the graph, the k-mer 'ATT' has multiple edges that correspond to it. WHen I follow the edges from this node, I get ATT TTC TCA CAT ATT TTG TGA GAT ATT TTT. Because these are k-mers, they have repeated regions. When I remove that, my final possible genome sequence would be 'ATTCATTCTTATTGATTT'. 


### Step 2.6 

#### Instructions : In a few sentences, what would it take to accurately reconstruct the sequence of the genome? Record your answer in your README.md.

ANSWER : To reconstruct the sequence of the genome in a more accurate manner, we would have to start with higher-quality precision methods in extracting the DNA, sequencing the extracted data with higher coverage long read sequencing technology, and then using more robust computational analysis. In addition to raising the rigor of the extraction and analysis of the reads, we would hve to include better protective measures of error control and detection methods for accurate reading of repeated regions. A possible good way to start would be using multiple types of long-read sequencing methods and overlapping the sequencing results to see the basis foundation. 
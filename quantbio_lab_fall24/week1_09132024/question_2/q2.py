#!/usr/bin/env python3

### EXERCISE 2 : DE BRUJIN GRAPH CONSRTUCTION 

## < STEP 2.1 > 

## Instructions : 
    # 1) Write a dictionary to find all edges in de brujin graph corresponding to provided reads using k = 3 (with format ATT -> TTC)
    # 2) Write all the found edges to a file, with each edge as its own line in the file 

# Import 'sys' package into current python envrionment 
import sys

# Taking the provided set of reads and putting it into a variable called 'reads' 
reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

# Our desired k-mer is 3 and so saving this value into the variable called 'k' 
k = 3 

# Printing my results to see that it properly saved 
print(reads) 
print(k)


# Creating a dictionary called 'edges'
edges = {}

# Writing a for loop to iterate over each read where the key = tupule of the overlapping k-mers 
for read in reads: 
    for i in range(len(read) - k): # Nested loop to iterate for the starting base of each read 
        kmer1 = read[i: i+k]
        kmer2 = read[i+1: i+1+k]
        edges.setdefault((kmer1, kmer2), 0) 
        edges[(kmer1, kmer2)] +=1 # Increasing count for an already present k-mer 


# Printing the length of edges to see how many there are in total and what the edges look like 
#print(len(edges))
#print(edges)

# Writing all the edges found in the 'edges' dictionary into a file called 'de_bruijn_graph_edges.txt' and saving each one as a new line 
# Left this code as comments because I rewrote it to create a dot plot for my answer to question 2.3 
#with open('de_bruijn_graph_edges.txt', 'w') as file:
    #for (kmer1, kmer2) in edges.keys():
        #file.write(f"{kmer1} -> {kmer2}\n") 



## < STEP 2.2 >

## Instructions: 
    # 1) Create a conda environment 
    # 2) Install graphviz 

# Used provided code in terminal to do this question 
#conda create -n graphviz -c conda-forge graphviz
#conda activate graphviz



## < STEP 2.3 > 

## Instructions:
    # 1) Modify code from step 2.1 to output the edges in a format that 'dot' can use


# Writing all the edges found in the 'edges' dictionary into a file called 'de_bruijn_graph_edges.txt' and saving each one as a new line 
with open("de_bruijn_graph_edges.dot", "w") as f:
    f.write("digraph {\n")
    for left, right in edges:
        f.write(f'    "{left}" -> "{right}" \n')  
    f.write("}\n")


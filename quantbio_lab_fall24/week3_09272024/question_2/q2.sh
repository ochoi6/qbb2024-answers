#!/usr/bin/env bash


#### < EXERCISE 2 : MAP READS TO THE REFERENCE GENOME > 


### STEP 2.1: Download and index the sacCer3 genome 

    # QUESTION 2.1 : How many chromsomes are in the yeast genome? 
    
        # ANSWER: 17 chromosomes 

        # Code used for question in question 2.1: grabbing any line that begins with 'chr' in it and counting using -c option command in the fasta genome file of yeast
        #grep -c "chr*" sacCer3.fa 


### STEP 2.2, 2.4: Align your reads to the reference + format and index those alignments 

# Created a for-loop that aligns reads using bwa and then sorting + formatting my reads using samtools based on the for-loop we did in class
for my_reads in *.fastq
do 
    my_reads=`basename ${my_reads} .fastq`
    # changed this portion because in class we used paired-end reads but this assignment is using single-end reads 
    bwa mem -R "@RG\tID:${my_reads}\tSM:${my_reads}" sacCer3.fa ${my_reads}.fastq > ${my_reads}.sam
    samtools sort -@ 4 -O bam -o ${my_reads}.bam ${my_reads}.sam
    samtools index ${my_reads}.bam 
done 



### STEP 2.3: Sanity check your alignments 

    # QUESTION 2.2 : How many total read alignments are recorded in the SAM file?  
    
        # ANSWER: 669548 read alignments. 

        # Code used for question in question 2.2: grabbing any line that begins with '@' in it and inverse counting (taking any lines that don't have the @) using -v option command and printing the results 
        #grep -v "^@" A01_09.sam | wc -l

    # QUESTION 2.3 : How many of the alignments are to loci on chromosome III?  
    
        # ANSWER: 7815 read alignments to loci on chromosome III.  

        # Code used for question in question 2.3: grabbing any line that contains tab-separated values of chrIII in the sam file and printing the result 



### STEP 2.5: Visualize alignments 

    # Instructions: 
        # 1) Open IGV and set the SacCer3 genome as the reference. 
        # 2) Load the sample A01_09 in IGV 
        # 3) Zoom in far enough to see the reads and scan through some alignments.


    # QUESTION 2.4 : Does the depth of coverage appear to match that which you estimated in Step 1.3? Why or why not? 
    
        # ANSWER: In general, the coverage does match the 4x coverage calculated in question 1. When I look at the small gray bars, there is at least 4 to 6 for each location, meaning the coverage range is around 4 to 5x for each read aligned. 

    # QUESTION 2.5 : Set your window to chrI:113113-113343 (paste that string in the search bar and click enter). How many SNPs do you observe in this window? Are there any SNPs about which you are uncertain? Explain your answer.
    
        # ANSWER: I see 3 SNPs. There is one SNP at chrI:113,259-113,334 that is only mutated twice that I am unsure about. Because it isn't a SNP through all reads, I am unsure if its just sequencing error or an actual indel. 

    # QUESTION 2.6 : Set your window to chrIV:825548-825931. What is the position of the SNP in this window? Does this SNP fall within a gene?
    
        # ANSWER: chrIV:825,834 and is in the intergenic region between SCC2 and SAS4.  



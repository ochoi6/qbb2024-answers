#!/usr/bin/bash


#### < EXERCISE 2 : Count feature SNPs and determining enrichment > 

# General overview - using datafiles from part 1 + SNP bed files partitioned by MAF:
    # 1) Find how many SNPs overlap each
    # 2) Finding the mean SNP/bp for each feature 
    # 3) Calculate enrichment of each feature SNP density for each MAF level 



### STEP 2.1 : Create a bash script to find overlap of SNPs, feature and calculate the SNP density enrichment for each MAF-feature combination

## Instructions:
    # 1) Write a bash script that loops through each MAF file and feature bed file using a for loop 
    # 2) Use command 'bedtools coverage' to find how many SNPs fall within each set of features (total count)
    # 3) Sum the number of SNPs and total size of feature + double check the output using 'awk' command 
    # 4) Calculate ratio of themse sums to determine SNP density using 'bc' command 
    # 5) Calculate enrichment value by divide by the background (background = total # SNPs for given MAF / chromosome length)
    # 6) Save results in a file called 'snp_counts.txt'
    # Total 5 SNP files with different MAF levels and 4 feature files = 20 total combinations
 

#Saving the results in a file called 'snp_counts.txt'
echo -e "MAF\tFeature\tEnrichment" > snp_counts.txt


maf_files=("chr1_snps_0.1.bed" "chr1_snps_0.2.bed" "chr1_snps_0.3.bed" "chr1_snps_0.4.bed" "chr1_snps_0.5.bed")
feature_files=("cCREs_chr1.bed" "exons_chr1.bed" "introns_chr1.bed" "other_chr1.bed")

for maf in 0.1 0.2 0.3 0.4 0.5;  
do 
    maf_file_name=chr1_snps_${maf}.bed
    # Calculate coverage and SNP density for the genome
    bedtools coverage -a genome_chr1.bed -b ${maf_file_name} > temp_file_${maf}.txt
    snp_sum_maf=$(awk '{s+=$4}END{print s}' temp_file_${maf}.txt)
    base_from_coverage_maf=$(awk '{s+=$6}END{print s}' temp_file_${maf}.txt)
    
    # Calculate genome-wide background SNP density
    background_maf=$(echo "${snp_sum_maf} / ${base_from_coverage_maf}" | bc -l)

    # Loop through each feature file
    for feature_file in cCREs exons introns other;
    do 
        feature_file_name=${feature_file}_chr1.bed
        # Calculate coverage and SNP density for the feature
        bedtools coverage -a ${feature_file_name} -b ${maf_file_name} > feature_temp_file${feature_file}.txt
        snp_sum_feature=$(awk '{s+=$4}END{print s}' feature_temp_file${feature_file}.txt)
        base_from_coverage_feature=$(awk '{s+=$6}END{print s}' feature_temp_file${feature_file}.txt)
        
        # Calculate feature SNP density
        feature_density=$(echo "${snp_sum_feature} / ${base_from_coverage_feature}" | bc -l)
        
        # Calculate enrichment (feature_density / background_maf)
        enrichment=$(echo "${feature_density} / ${background_maf}" | bc -l)

        # Append results to the output file
        echo -e "${maf}\t${feature_file}\t${enrichment}" >> snp_counts.txt
    done
done



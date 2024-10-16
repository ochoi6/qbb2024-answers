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
 

# Creating a header in the new file containing output called 'snp_counts.txt' with 3 columns "MAF", "Feature", and "Enrichment" that are separated by tabs
echo -e "MAF\tFeature\tEnrichment" > snp_counts.txt

# Creating respective arrays to store the list of MAF (there should be a total of 4 files) and feature (there should be a total of 4) files 
maf_files=("chr1_snps_0.1.bed" "chr1_snps_0.2.bed" "chr1_snps_0.3.bed" "chr1_snps_0.4.bed" "chr1_snps_0.5.bed")
feature_files=("cCREs_chr1.bed" "exons_chr1.bed" "introns_chr1.bed" "other_chr1.bed")

# Creating a for loop that runs through each individual maf file in the array of maf files 
for maf in 0.1 0.2 0.3 0.4 0.5;  
do 

    # Creating a file name for the maf file being run through with the synonymous parts of name written out and creating a parameter to substitute each new file respectively 
    maf_file_name=chr1_snps_${maf}.bed

    # Calculating bedtools coverage for the genome of chromosome 1 using bedtools and inputting the output of that into a new temp file for each maf file
    bedtools coverage -a genome_chr1.bed -b ${maf_file_name} > temp_file_${maf}.txt

    # Summing the SNP counts using the 4th column from the output saved in the respective temp maf files and storing it in a variable called 'snp_sum_maf'
    snp_sum_maf=$(awk '{s+=$4}END{print s}' temp_file_${maf}.txt)

    # Summing the base coverage counts using the 6th column from the output saved in the respective temp maf file and storing it in a variable called 'base_from_coverage_maf'
    base_from_coverage_maf=$(awk '{s+=$6}END{print s}' temp_file_${maf}.txt)
    
    # Calculating genome-wide background SNP density using the equation + the necessary command options provided and storing it into a variable called 'background_maf'
    background_maf=$(echo -e "${snp_sum_maf} / ${base_from_coverage_maf}" | bc -l)

    # Looping through each feature file in the array of feature files using a nested for loop 
    for feature_file in cCREs exons introns other;
    do 
        # Creating a file name for the feature file being run through with the synonymous parts of name written out and creating a parameter to substitute each new file respectively 
        feature_file_name=${feature_file}_chr1.bed

        # Calculating bedtools coverage for the specific feature in chromosome 1 using bedtools and inputting the output of that into a feature new temp file for each feature file
        bedtools coverage -a ${feature_file_name} -b ${maf_file_name} > feature_temp_file${feature_file}.txt

        # Summing the SNP counts using the 4th column from the output saved in the respective temp feature files and storing it in a variable called 'snp_sum_feature'
        snp_sum_feature=$(awk '{s+=$4}END{print s}' feature_temp_file${feature_file}.txt)

        # Summing the base coverage counts using the 6th column from the output saved in the respective temp maf file and storing it in a variable called 'base_from_coverage_feature'
        base_from_coverage_feature=$(awk '{s+=$6}END{print s}' feature_temp_file${feature_file}.txt)
        
        # Calculating the feature SNP density using the equation + necessary command options provided and storing it into a variable called 'feature_density'
        feature_density=$(echo "${snp_sum_feature} / ${base_from_coverage_feature}" | bc -l)
        
        # Calculating enrichment using this equation enrichment = feature_density / background_maf and storing it into a variable called 'enrichment'
        enrichment=$(echo -e "${feature_density} / ${background_maf}" | bc -l)

        # Appending the results to the output file 'snp_counts.txt'
        echo -e "${maf}\t${feature_file}\t${enrichment}" >> snp_counts.txt
    done
done



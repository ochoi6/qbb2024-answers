#!/bin/bash

#### < EXERCISE 1 : Obtain the data > 


### STEP 1.1 : Download data 

## Instructions:
    # 1) Download snp files from given link and untar it using the command 'tar xzf chr1_snps.tar.gz'
    # There be a total of 6 files (5 files for chromosome 1 snp values 1 to 5 + genome chromosome 1 file)

# Untarring the zip file to release the 6 SNP bed files 
#tar xzf chr1_snps.tar.gz

# Printing all 5 chromosmoe 1 snp files to see that it was correctly loaded 
#head chr1_snps_*.bed  
#==> chr1_snps_0.1.bed <==
#chr1	11007	11008	rs575272151	0.0880591	.
#chr1	11011	11012	rs544419019	0.0880591	.
#chr1	13109	13110	rs540538026	0.0267572	.
#chr1	13115	13116	rs62635286	0.0970447	.
#chr1	13117	13118	rs62028691	0.0970447	.
#chr1	13272	13273	rs531730856	0.0950479	.
#chr1	14463	14464	rs546169444	0.0958466	.
#chr1	14932	14933	rs199856693	0.0283546	.
#chr1	15773	15774	rs374029747	0.0119808	.
#chr1	15776	15777	rs2691317	0.0283546	.

#==> chr1_snps_0.2.bed <==
#chr1	14598	14599	rs707680	0.147564	.
#chr1	14603	14604	rs541940975	0.147564	.
#chr1	30922	30923	rs806731	0.127596	.
#chr1	51478	51479	rs116400033	0.128195	.
#chr1	58813	58814	rs114420996	0.109026	.
#chr1	63670	63671	rs80011619	0.1875	.
#chr1	86330	86331	rs115209712	0.113019	.
#chr1	89945	89946	rs138808727	0.122604	.
#chr1	92857	92858	rs147061536	0.134984	.
#chr1	95439	95440	rs544194668	0.151158	.

#==> chr1_snps_0.3.bed <==
#chr1	49297	49298	rs10399793	0.217851	.
#chr1	54715	54716	rs569128616	0.289137	.
#chr1	55544	55545	rs28396308	0.239217	.
#chr1	62776	62777	rs3844233	0.25639	.
#chr1	88168	88169	rs940550	0.299321	.
#chr1	122871	122872	rs62642125	0.235623	.
#chr1	125270	125271	rs3871807	0.223243	.
#chr1	158005	158006	rs78348422	0.283546	.
#chr1	263721	263722	rs112455420	0.209065	.
#chr1	611424	611425	rs61769283	0.225639	.

#==> chr1_snps_0.4.bed <==
#chr1	15210	15211	rs3982632	0.390974	.
#chr1	15273	15274	rs2758118	0.347244	.
#chr1	63267	63268	rs28664618	0.353035	.
#chr1	63735	63741	rs61158452	0.371805	.
#chr1	69896	69897	rs200676709	0.311901	.
#chr1	83513	83514	rs201754587	0.372404	.
#chr1	104185	104186	rs4288537	0.399361	.
#chr1	600714	600715	rs189259765	0.398163	.
#chr1	611421	611422	rs113633859	0.323283	.
#chr1	629625	629626	rs1856864	0.385583	.

#==> chr1_snps_0.5.bed <==
#chr1	10177	10179	rs367896724	0.425319	.
#chr1	10352	10353	rs555500075	0.4375	.
#chr1	14929	14930	rs6682385	0.482228	.
#chr1	15819	15820	rs2691315	0.410543	.
#chr1	15903	15905	rs557514207	0.441094	.
#chr1	54712	54774	rs201095316	0.420128	.
#chr1	91514	91515	rs376723915	0.426717	.
#chr1	91535	91536	rs6702460	0.420727	.
#chr1	91580	91581	rs1524604	0.423722	.
#chr1	129010	129015	rs377161483	0.488419	.

#head genome_chr1.bed 
#chr1	0	20000
#chr1	20000	40000
#chr1	40000	60000
#chr1	60000	80000
#chr1	80000	100000
#chr1	100000	120000
#chr1	120000	140000
#chr1	140000	160000
#chr1	160000	180000
#chr1	180000	200000



### STEP 1.2 : Download feature files using UCSC genome table browser 

## Instructions:
    # 1) Download gencode v46 known genes from 'Genes and Gene Predictions' for chromome 1 
    # 2) In output format, select 'Selected fields from the primary and related tables'
    # 3) For gene bed file, select for chromosome, txStart (transcription start), and txEnd (transcription end) positions
    # 4) Repeat steps 1 to 3 and to create a exons bed file, select for chromosome, exonStarts, and exonEnds



### STEP 1.3 : Use table browser to obtain Encode cCREs 

## Instructions:
    # 1) Download the set of regulatory elements using the UCSC table browser using instructions from step 1.2 instruction numbers 1 to 3
    # 2) Make sure to select for 'Regulation' under 'Encode cCREs'
    # 4) Select for chromosome, chromStart, and chromEnd fields



### STEP 1.4 : Use bedtools to merge elements within each feature file 

## Instructions:
    # 1) Use 'bedtools sort' command on each feature file
    # 2) Use 'bedtools merge' command on each feature file 
    # 3) Save the final output after the 2 commands above as <feature>_chr1.bed where <feature> is each feature name (genes, exons, or cCREs) for a total of 3 files

# Using 'bedtools sort' command to sort each feature file and saving it as <feature>_sorted.bed format
bedtools sort -i cCREs.bed > cCREs_sorted.bed
bedtools sort -i exons.bed > exons_sorted.bed
bedtools sort -i genes.bed > genes_sorted.bed

# Using 'bedtools merge' command to merge each sorted feature file and saving it as <feature>_chr1.bed format
bedtools merge -i cCREs_sorted.bed > cCREs_chr1.bed
bedtools merge -i exons_sorted.bed > exons_chr1.bed
bedtools merge -i genes_sorted.bed > genes_chr1.bed

# Printing that there are now 3 total sorted and merged files
#ls *_chr1.bed 
#cCREs_chr1.bed	exons_chr1.bed	genes_chr1.bed

# Printing each feature file's output to see that the 2 commands done above worked
#head *_chr1.bed
#==> cCREs_chr1.bed <==
#chr1	181251	181601
#chr1	190865	191071
#chr1	778562	778912
#chr1	779086	779355
#chr1	779727	780060
#chr1	790397	790626
#chr1	807736	807916
#chr1	812113	812266
#chr1	817080	817403
#chr1	817903	818252

#==> exons_chr1.bed <==
#chr1	65564	65573
#chr1	69036	70008
#chr1	450739	451678
#chr1	685715	686654
#chr1	924431	924948
#chr1	925921	926013
#chr1	930154	930336
#chr1	931038	931089
#chr1	935771	935896
#chr1	939039	939129

#==> genes_chr1.bed <==
#chr1	11868	14409
#chr1	14695	24886
#chr1	29553	31109
#chr1	34553	36081
#chr1	52472	53312
#chr1	57597	64116
#chr1	65418	71585
#chr1	89294	134836
#chr1	135140	135895
#chr1	137681	137965

# Printing the whole directory to see my file and their respective sizes to gauge that the merge and sorted worked
#ls -l
#total 39360
#-rw-r--r--@ 1 cmdb  staff  1999823 Sep 20 12:04 cCREs.bed
#-rw-r--r--  1 cmdb  staff  1994672 Sep 22 17:56 cCREs_chr1.bed
#-rw-r--r--  1 cmdb  staff  1994672 Sep 22 17:56 cCREs_sorted.bed
#-rw-r--r--@ 1 cmdb  staff  6058893 Sep 20 12:02 exons.bed
#-rw-r--r--  1 cmdb  staff   519268 Sep 22 17:59 exons_chr1.bed
#-rw-r--r--  1 cmdb  staff  6058893 Sep 22 17:58 exons_sorted.bed
#-rw-r--r--@ 1 cmdb  staff   542483 Sep 20 12:01 genes.bed
#-rw-r--r--  1 cmdb  staff    74174 Sep 20 12:22 genes_chr1.bed
#-rw-r--r--  1 cmdb  staff    74174 Sep 20 12:23 genes_sorted.bed



### STEP 1.5 : Use bedtools to create intron feature file 

## Instructions:
    # 1) Using the merged gene and exon files created in step 1.4, subtract exonic intervals from gene intervals using the command 'bedtools subtract'
    # 2) Save the output for this into a file called 'introns_chr1.bed'

# Using 'bedtools subtract' command to subtract exonic intervals from gene intervals and saving this output into a file called 'introns_chr1.bed'
bedtools subtract -a genes_chr1.bed -b exons_chr1.bed > introns_chr1.bed

# Printing 'introns_chr1.bed' to see if it was done correctly with no errors 
#head introns_chr1.bed
#chr1	11868	14409
#chr1	14695	24886
#chr1	29553	31109
#chr1	34553	36081
#chr1	52472	53312
#chr1	57597	64116
#chr1	65418	65564
#chr1	65573	69036
#chr1	70008	71585
#chr1	89294	134836



### STEP 1.6 : Use bedtools to find intervals not covered by other features 

## Instructions:
    # 1) Using the 'genome_chr1.bed' file, subtract the exon, intron, and cCRE files from it using the command 'bedtools subtract'
    # 2) Save the output for this in 'other_chr1.bed' 

# Using 'bedtools subtract' command  and subtracting exons, introns, and cCRE from the overall genome chromosome 1 file and saving this output into a new file called 'other_chr1.bed'
bedtools subtract -a /Users/cmdb/qbb2024-answers/quantbio_lab_fall24/week2_09202024/question_1/SNP_files/genome_chr1.bed -b exons_chr1.bed -b introns_chr1.bed -b cCREs_chr1.bed > other_chr1.bed

# Printing 'other_chr1.bed' to see if it was done correctly 
#head other_chr1.bed 
#chr1	0	11868
#chr1	14409	14695
#chr1	24886	29553
#chr1	31109	34553
#chr1	36081	40000
#chr1	40000	52472
#chr1	53312	57597
#chr1	64116	65418
#chr1	71585	80000
#chr1	80000	89294

#!/bin/bash

(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools sort -i cCREs_merged.bed > cCREs_sorted.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ls
cCREs.bed		cCREs_sorted.bed	genes.bed		genes_sorted.bed
cCREs_merged.bed	exons.bed		genes_merged.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ls -l
total 26480
-rw-r--r--@ 1 cmdb  staff  1999823 Sep 20 12:04 cCREs.bed
-rw-r--r--  1 cmdb  staff  1994672 Sep 22 17:56 cCREs_merged.bed
-rw-r--r--  1 cmdb  staff  1994672 Sep 22 17:56 cCREs_sorted.bed
-rw-r--r--@ 1 cmdb  staff  6058893 Sep 20 12:02 exons.bed
-rw-r--r--@ 1 cmdb  staff   542483 Sep 20 12:01 genes.bed
-rw-r--r--  1 cmdb  staff    74174 Sep 20 12:22 genes_merged.bed
-rw-r--r--  1 cmdb  staff    74174 Sep 20 12:23 genes_sorted.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools merge -i exons.bed > exons_merged.bed
Error: Sorted input specified, but the file exons.bed has the following out of order record
chr1	924431	924948	ENST00000618323.5_cds_0_0_chr1_924432_f	0	+
(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools merge -i exons.bed > exons_merged.bed 
Error: Sorted input specified, but the file exons.bed has the following out of order record
chr1	924431	924948	ENST00000618323.5_cds_0_0_chr1_924432_f	0	+
(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools sort -i exons.bed > exons_sorted.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools merge -i exons_sorted.bed > exons_merged.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ls -l
total 39360
-rw-r--r--@ 1 cmdb  staff  1999823 Sep 20 12:04 cCREs.bed
-rw-r--r--  1 cmdb  staff  1994672 Sep 22 17:56 cCREs_merged.bed
-rw-r--r--  1 cmdb  staff  1994672 Sep 22 17:56 cCREs_sorted.bed
-rw-r--r--@ 1 cmdb  staff  6058893 Sep 20 12:02 exons.bed
-rw-r--r--  1 cmdb  staff   519268 Sep 22 17:59 exons_merged.bed
-rw-r--r--  1 cmdb  staff  6058893 Sep 22 17:58 exons_sorted.bed
-rw-r--r--@ 1 cmdb  staff   542483 Sep 20 12:01 genes.bed
-rw-r--r--  1 cmdb  staff    74174 Sep 20 12:22 genes_merged.bed
-rw-r--r--  1 cmdb  staff    74174 Sep 20 12:23 genes_sorted.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % head exons_merged.bed
chr1	65564	65573
chr1	69036	70008
chr1	450739	451678
chr1	685715	686654
chr1	924431	924948
chr1	925921	926013
chr1	930154	930336
chr1	931038	931089
chr1	935771	935896
chr1	939039	939129
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ls
cCREs.bed		cCREs_sorted.bed	exons_merged.bed	genes.bed		genes_sorted.bed
cCREs_merged.bed	exons.bed		exons_sorted.bed	genes_merged.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ls
cCREs.bed	exons.bed	genes.bed	q1.sh
(qb24) cmdb@QuantBio-24 ucsc_feature_files % chmod +x q1.sh    
(qb24) cmdb@QuantBio-24 ucsc_feature_files % cd ..
(qb24) cmdb@QuantBio-24 ~ % ls
Applications			Music				Sites
Data				Obsidian			qbb2024
Desktop				OneDrive - Johns Hopkins	qbb2024-answers
Documents			Pictures			quant_bio
Downloads			Public				quantbio_lab_fall24_notes
Farber				R				ucsc_feature_files
Library				RCR end of semester quiz.pdf	vsc
Movies				SNP_files
(qb24) cmdb@QuantBio-24 ~ % cd SNP_files 
(qb24) cmdb@QuantBio-24 SNP_files % ls
chr1_snps.tar.gz	chr1_snps_0.2.bed	chr1_snps_0.4.bed	genome_chr1.bed
chr1_snps_0.1.bed	chr1_snps_0.3.bed	chr1_snps_0.5.bed
(qb24) cmdb@QuantBio-24 SNP_files % cd ..
(qb24) cmdb@QuantBio-24 ~ % ls
Applications			Music				Sites
Data				Obsidian			qbb2024
Desktop				OneDrive - Johns Hopkins	qbb2024-answers
Documents			Pictures			quant_bio
Downloads			Public				quantbio_lab_fall24_notes
Farber				R				ucsc_feature_files
Library				RCR end of semester quiz.pdf	vsc
Movies				SNP_files
(qb24) cmdb@QuantBio-24 ~ % cd ucsc_feature_files 
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ls
cCREs.bed	exons.bed	genes.bed	q1.sh
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ./q1.sh 
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ./q1.sh
(qb24) cmdb@QuantBio-24 ucsc_feature_files % chmod +x q1.sh 
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ./q1.sh       
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ./q1.sh
(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools --version
bedtools v2.31.1
(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools sort -i cCREs.bed > cCREs_sorted.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools sort -i exons.bed > exons_sorted.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools sort -i genes.bed > genes_sorted.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ls -l
total 35208
-rw-r--r--@ 1 cmdb  staff  1999823 Sep 20 12:04 cCREs.bed
-rw-r--r--  1 cmdb  staff  1999796 Sep 22 20:11 cCREs_sorted.bed
-rw-r--r--@ 1 cmdb  staff  6058893 Sep 20 12:02 exons.bed
-rw-r--r--  1 cmdb  staff  6058893 Sep 22 20:11 exons_sorted.bed
-rw-r--r--@ 1 cmdb  staff   542483 Sep 20 12:01 genes.bed
-rw-r--r--  1 cmdb  staff   542462 Sep 22 20:11 genes_sorted.bed
-rwxr-xr-x@ 1 cmdb  staff       13 Sep 22 19:48 q1.sh
(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools merge -i cCREs_sorted.bed > cCREs_merged.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools merge -i exons_sorted.bed > exons_merged.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools merge -i genes_sorted.bed > genes_merged.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ls -l
total 40272
-rw-r--r--@ 1 cmdb  staff  1999823 Sep 20 12:04 cCREs.bed
-rw-r--r--  1 cmdb  staff  1994672 Sep 22 20:15 cCREs_merged.bed
-rw-r--r--  1 cmdb  staff  1999796 Sep 22 20:11 cCREs_sorted.bed
-rw-r--r--@ 1 cmdb  staff  6058893 Sep 20 12:02 exons.bed
-rw-r--r--  1 cmdb  staff   519268 Sep 22 20:15 exons_merged.bed
-rw-r--r--  1 cmdb  staff  6058893 Sep 22 20:11 exons_sorted.bed
-rw-r--r--@ 1 cmdb  staff   542483 Sep 20 12:01 genes.bed
-rw-r--r--  1 cmdb  staff    74174 Sep 22 20:15 genes_merged.bed
-rw-r--r--  1 cmdb  staff   542462 Sep 22 20:11 genes_sorted.bed
-rwxr-xr-x@ 1 cmdb  staff       13 Sep 22 19:48 q1.sh
(qb24) cmdb@QuantBio-24 ucsc_feature_files % cp cCREs_merged.bed cCREs_chr1.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % cp exons_merged.bed exons_chr1.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % cp genes_merged.bed genes_chr1.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % head *_chr1.bed
==> cCREs_chr1.bed <==
chr1	181251	181601
chr1	190865	191071
chr1	778562	778912
chr1	779086	779355
chr1	779727	780060
chr1	790397	790626
chr1	807736	807916
chr1	812113	812266
chr1	817080	817403
chr1	817903	818252

==> exons_chr1.bed <==
chr1	65564	65573
chr1	69036	70008
chr1	450739	451678
chr1	685715	686654
chr1	924431	924948
chr1	925921	926013
chr1	930154	930336
chr1	931038	931089
chr1	935771	935896
chr1	939039	939129

==> genes_chr1.bed <==
chr1	11868	14409
chr1	14695	24886
chr1	29553	31109
chr1	34553	36081
chr1	52472	53312
chr1	57597	64116
chr1	65418	71585
chr1	89294	134836
chr1	135140	135895
chr1	137681	137965
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ls head *_chr1.bed
ls: head: No such file or directory
cCREs_chr1.bed	exons_chr1.bed	genes_chr1.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ls *_chr1.bed 
cCREs_chr1.bed	exons_chr1.bed	genes_chr1.bed

(qb24) cmdb@QuantBio-24 ucsc_feature_files % bedtools subtract -a genes_chr1.bed -b exons_chr1.bed > introns_chr1.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % ls introns_chr1.bed
introns_chr1.bed
(qb24) cmdb@QuantBio-24 ucsc_feature_files % head introns_chr1.bed
chr1	11868	14409
chr1	14695	24886
chr1	29553	31109
chr1	34553	36081
chr1	52472	53312
chr1	57597	64116
chr1	65418	65564
chr1	65573	69036
chr1	70008	71585
chr1	89294	134836
(qb24) cmdb@QuantBio-24 ucsc_feature_files % cd ..           
(qb24) cmdb@QuantBio-24 ~ % ls
Applications			Music				q1.sh
Data				Obsidian			qbb2024
Desktop				OneDrive - Johns Hopkins	qbb2024-answers
Documents			Pictures			quant_bio
Downloads			Public				quantbio_lab_fall24_notes
Farber				R				ucsc_feature_files
Library				RCR end of semester quiz.pdf	vsc
Movies				Sites
(qb24) cmdb@QuantBio-24 ~ % mkdir ucsc_final_feature_files
(qb24) cmdb@QuantBio-24 ~ % bedtools subtract -a /Users/cmdb/qbb2024-answers/quantbio_lab_fall24/week2_09202024/question_1/SNP_files/genome_chr1.bed -b exons_chr1.bed -b introns_chr1.bed -b cCREs_chr1.bed > other_chr1.bed

head other_chr1.bed 

chr1	0	11868
chr1	14409	14695
chr1	24886	29553
chr1	31109	34553
chr1	36081	40000
chr1	40000	52472
chr1	53312	57597
chr1	64116	65418
chr1	71585	80000
chr1	80000	89294




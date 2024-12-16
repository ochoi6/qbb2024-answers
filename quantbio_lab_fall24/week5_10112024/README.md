#  WEEK 5 EXERCISE ANSWERS 

## Exercise 1 : Checking fastq quality 

### Step 1.1 - Open fastqc and load both sample files from the File menu 

#### Question : Do any stand out as problematic? Can you think of a reason why this sample does not match the expected GC content distribution and base content at the beginning of sequences?

#### Answer : It seems that these 2 things don't match the expected because the RNA-sequencing data for this is specifically from Drosophila midgut rather than from all tissue samples, leading to genome-woide expectations not matching up here in this instance. Thus in the fastqc report, the per base sequence content and per sequence GC content seem to stand out. 

### Step 1.2 - Overrepresented sequences 

#### Question : What is the origin of the most overrepresented sequence in this sample? Does it make sense?

#### Answer : The most overrepresented sequence has 27 counts and is from Drosophila. This makes sense because our sample was taken from Drosophila. The sequence encodes for serine proteases and biologically this makes sense because of their function as digestive enzymes (common ones being trypsin and chymotrypsin for example). 


## Exercise 2 : Using MultiQC to check processed data quality

#### Question : If you were to reject any samples with the percentage of unique reads less than 45%, how many samples would you keep?

#### Answer : Based on the html file, the STAR % aligned column contains samples with percentage of unique reads mapped. Within the tissue triplicates, there seems to be some inconsistent trends where it would be 67, 56, and then 81% read alignment. Since there are 30 samples, only half of them pass the cut-off. 

#### Question : Can you see the blocks of triplicates clearly? Try adjusting the min slider up. Does this suggest anything about consistency between replicates?

#### Answer : The blocks of triplicates are clearly visible. There are a couple of samples in the slight middle left and right portion are slightly fainter, but overall it is distinct. This suggests that there is high consistency between the replicates. 

## Exercise 3 : Normalization and clustering

### Step 3.3 - PCA analysis 

#### Question : Examine the PCA plot. Does everything look okay (We wouldn’t ask if it did)? What does the PCA plot suggest to you about the data? Why?

#### Answer : LFC-Fe replicate 3 and Fe replicate 1 seem to be labeled incorrectly because they are clustered with the wrong groups. LFC-Fe replicate 3 is clustered together to Fe replicates 1,2 and Fe replicate 1 is clustered together to LFC-Fe replicates 2,3. 

### Step 3.6 - Gene ontology enrichment analysis

#### Question : Do the categories of enrichments make sense? Why? 

#### Answer : Yes, the enrichment categories make sense because most of them fall under metabolic processes such as ethanol metabolic process, carbohydrate catabolic process, digestive system/tract development, etc. Because our sample is from midgut, we shoulde expect most of the results to be related to digestion related metabolic and oxidative processes. 

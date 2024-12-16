#!/usr/bin/env python

### Description: 

    # 24 single-channel images 
    # 4 different samples that each have 2 separate fields 
    # each sample-field has 3 channel images (DAPI, Alexa568, EU-Alexa488)


### EXERCISE 1: LOADING THE IMAGE DATA 

# Directions: create a for-loop that...
    # Load the channel images into python with imageio.v3.imread function
    # Loop through list of gene names 
    # For each gene/field -> put all of the channels into same array so that image is (X, Y, 3) -> (width, height, # channels)
    # Should result in 8 x 3-colored image arrays 


# Importing all the necessary packages into the current environment 

import numpy
import matplotlib.pyplot as plt
import imageio
import plotly
import plotly.express as px
import cvs


# Creating an empty list to store the images 
all_images = []


# Creating a list called 'genes' and storing the 4 genes in it 
genes = ["APEX1", "PIM2", "POLR2B", "SRSF1"]

# Printing the created 'gene' list to ensure it worked 
print(genes)


# Creating a list called 'fields' and storing the 2 fields in it
fields = ["field0", "field1"]

# Printing the created 'fields' list to ensure it worked 
print(fields) 


# Creating a list called 'channels' and storing the 3 channels in it 
channels = ["DAPI", "nascentRNA", "PCNA"]

# Printing the created 'channels' list to ensure it worked 
print(channels)


# Creating and intializing an empty dictionary callde 'imgArray' 
imgArray = {}


# Creating a for-loop to load channel images into python 
for gene in genes:

    # Dimensions of the image might change depending on the gene and so running a trial with one of the images  
    trial = imageio.v3.imread(f"{gene}_field0_DAPI.tif")

    # Shape method -> to grab the width and the height of an image and storing it into dimensions variable 
    dimensions = trial.shape
    imgArray[gene] = []

    # Creating a nested for-loop 
    for field in fields:

        # Initializing a 3-channel image array filled with zeros and the dimenbsions that we stored previously (width, height)
        imgArray[gene].append(numpy.zeros((dimensions[0], dimensions[1], 3), numpy.uint16))

        # Using enumerate in this step -> function: for a given vector or list, it will return an element and index to iterate through it 
        # Going through channels, DAPi in C and 0 in j 
        for j, channel in enumerate(channels):  
            # j contains the channel index 
            # Single pass through these 3 loops, now we have 4 variables to create a complex array that we were intially talking about 
            # For each channel of each gene of every field, we increment [i]
            imgArray[gene][-1][:, :, j] = imageio.v3.imread(f"{gene}_{field}_{channel}.tif")
            
            # Printing the imgArray created 
            print(imgArray)


### EXERCISE 2: IDENTIFYING INDIVIDUAL CELLS 

# Directions: using the segmentation function used in live-coding to identify and filter cells to remove outliers 
    # 2.1 - create a mask image to indicate nucleus vs background by using the mean value of an image's DAPI channel as a cutoff (gives a binary array with either True or False)
    # 2.2 - use 'find_labels' function to create a label map from DAPI mask with shape (X, Y) with zeros in all non-cell positions and positive numbers dnoting pixels belonging to a given nucleus 
          # use 'matplotlib.pyplot.imshow(label_array); matplot.pyplot.show()' and 'label_array[numpy.where(label_array == 0)] -= 50'
    # 2.3 - filter out labeled outliers based on size using 'filter_by_size' function ( < 100) + find size using 'bincount' + filter labels using 'mean size plus or minus the standard deviation of sizes as the lower and upper boundaries'
          # array method ravel(), e.g. passing the argument label_array.ravel() to bincount

## Step 2.1: For each image, create a binary mask from the DAPI channel

# Intializing an empty dictionary called 'masks'
masks = {}

# Creating a for-loop for every gene and field respectively in the imgArray dictionary made in exercise 1 
for gene, fields in imgArray.items():
    # Creating an empty list to store the binary mask for each field of each gene 
    masks[gene] = []
    # Nested for-loop 
    for field_array in fields:
        # Extracting the DAPI channel (index 0)
        dapi_image = field_array[:, :, 0]
        # Calculating the mean intensity value of the DAPI channel
        mean_intensity = numpy.mean(dapi_image)
        # Creating a binary mask: nucleus (True) vs. background (False)
        binary_mask = dapi_image > mean_intensity
        # Appending the binary mask to the list for the current gene 
        masks[gene].append(binary_mask)

## Step 2.2: Find labels for each image based on the DAPI mask from step 2.1 

# Segmentation for-loop copied from class live-coding section 
def find_labels(mask):
    # Set initial label
    l = 0
    # Create array to hold labels
    labels = numpy.zeros(mask.shape, numpy.int32)
    # Create list to keep track of label associations
    equivalence = [0]
    # Check upper-left corner
    if mask[0, 0]:
        l += 1
        equivalence.append(l)
        labels[0, 0] = l
    # For each non-zero column in row 0, check back pixel label
    for y in range(1, mask.shape[1]):
        if mask[0, y]:
            if mask[0, y - 1]:
                # If back pixel has a label, use same label
                labels[0, y] = equivalence[labels[0, y - 1]]
            else:
                # Add new label
                l += 1
                equivalence.append(l)
                labels[0, y] = l
    # For each non-zero row
    for x in range(1, mask.shape[0]):
        # Check left-most column, up  and up-right pixels
        if mask[x, 0]:
            if mask[x - 1, 0]:
                # If up pixel has label, use that label
                labels[x, 0] = equivalence[labels[x - 1, 0]]
            elif mask[x - 1, 1]:
                # If up-right pixel has label, use that label
                labels[x, 0] = equivalence[labels[x - 1, 1]]
            else:
                # Add new label
                l += 1
                equivalence.append(l)
                labels[x, 0] = l
        # For each non-zero column except last in nonzero rows, check up, up-right, up-right, up-left, left pixels
        for y in range(1, mask.shape[1] - 1):
            if mask[x, y]:
                if mask[x - 1, y]:
                    # If up pixel has label, use that label
                    labels[x, y] = equivalence[labels[x - 1, y]]
                elif mask[x - 1, y + 1]:
                    # If not up but up-right pixel has label, need to update equivalence table
                    if mask[x - 1, y - 1]:
                        # If up-left pixel has label, relabel up-right equivalence, up-left equivalence, and self with smallest label
                        labels[x, y] = min(equivalence[labels[x - 1, y - 1]], equivalence[labels[x - 1, y + 1]])
                        equivalence[labels[x - 1, y - 1]] = labels[x, y]
                        equivalence[labels[x - 1, y + 1]] = labels[x, y]
                    elif mask[x, y - 1]:
                        # If left pixel has label, relabel up-right equivalence, left equivalence, and self with smallest label
                        labels[x, y] = min(equivalence[labels[x, y - 1]], equivalence[labels[x - 1, y + 1]])
                        equivalence[labels[x, y - 1]] = labels[x, y]
                        equivalence[labels[x - 1, y + 1]] = labels[x, y]
                    else:
                        # If neither up-left or left pixels are labeled, use up-right equivalence label
                        labels[x, y] = equivalence[labels[x - 1, y + 1]]
                elif mask[x - 1, y - 1]:
                    # If not up, or up-right pixels have labels but up-left does, use that equivalence label
                    labels[x, y] = equivalence[labels[x - 1, y - 1]]
                elif mask[x, y - 1]:
                    # If not up, up-right, or up-left pixels have labels but left does, use that equivalence label
                    labels[x, y] = equivalence[labels[x, y - 1]]
                else:
                    # Otherwise, add new label
                    l += 1
                    equivalence.append(l)
                    labels[x, y] = l
        # Check last pixel in row
        if mask[x, -1]:
            if mask[x - 1, -1]:
                # if up pixel is labeled use that equivalence label 
                labels[x, -1] = equivalence[labels[x - 1, -1]]
            elif mask[x - 1, -2]:
                # if not up but up-left pixel is labeled use that equivalence label 
                labels[x, -1] = equivalence[labels[x - 1, -2]]
            elif mask[x, -2]:
                # if not up or up-left but left pixel is labeled use that equivalence label 
                labels[x, -1] = equivalence[labels[x, -2]]
            else:
                # Otherwise, add new label
                l += 1
                equivalence.append(l)
                labels[x, -1] = l
    equivalence = numpy.array(equivalence)
    # Go backwards through all labels
    for i in range(1, len(equivalence))[::-1]:
        # Convert labels to the lowest value in the set associated with a single object
        labels[numpy.where(labels == i)] = equivalence[i]
    # Get set of unique labels
    ulabels = numpy.unique(labels)
    for i, j in enumerate(ulabels):
        # Relabel so labels span 1 to # of labels
        labels[numpy.where(labels == j)] = i
    return labels

# Intializing an empty dictionary called 'label_maps'
label_maps = {}

# Looping through each gene and its corresponding list of masks in the masks dictionary
for gene, field_masks in masks.items():
    # Creating an empty 'label_maps' list 
    label_maps[gene] = []
    # Nested for-loop 
    for mask in field_masks:
        # Using the find_labels function to label nuclei
        label_array = find_labels(mask)
        # Show the label array with a color map (tab20)
        plt.imshow(label_array, cmap="tab20")
        plt.title(f"Label Map for {gene}")
        plt.colorbar()
        plt.show()

        # Adjusting labels (subtract 50 where label is non-zero)
        label_array[numpy.where(label_array > 0)] -= 50
        label_maps[gene].append(label_array)



## Step 2.3: Filter out labeled outliers based on size

# Filtering out outliers by size boundaries defined 
def filter_by_size(label_array, size_bounds):
    # Counting the number of pixels for each label (region)
    label_sizes = numpy.bincount(label_array.ravel())

    # Identifying labels that fall within these size bounds 
    valid_labels = [i for i, size in enumerate(label_sizes) if size_bounds[0] <= size <= size_bounds[1]]

    # Creating an empty array to store the filtered labels from before 
    filtered_labels = numpy.zeros_like(label_array)
    
    # Assigning labels to the corresponding regions in the filtered label array using a for-loop 
    for label in valid_labels:
        filtered_labels[label_array == label] = label
    # Returning the result 
    return filtered_labels

# Creating an empty dictionary to store filtered label maps for each gene
filtered_label_maps = {}

# Iterating through each gene using a for-loop 
for gene in genes:
    # Iterating through each field using a for-loop of each gene 
    for field_index, field in enumerate(fields):
        # Extracting DAPI channel rom the image
        dapi_image = imgArray[gene][field_index][:, :, 0]
        
        # Creating a binary mask for nucleus vs background based on mean intensity
        mask = dapi_image > numpy.mean(dapi_image)
        
        # Using find_labels function to label the nuclei in the binary mask
        label_array = find_labels(mask)
        
        # Checking that the label array contains only non-negative integers (background is 0)
        label_array = numpy.clip(label_array, 0, None)
        
        # Displaying again the labeled array with a set python color scheme package and title 
        plt.imshow(label_array, cmap="viridis")  
        plt.title(f"Labeled Image: {gene}, {field}")  
        plt.show()  

        # Computing sizes of labeled regions (excluding background)
        sizes = numpy.bincount(label_array.ravel())
        
        # Calculating the mean and standard deviation of the sizes of non-background labels
        mean_size = sizes[1:].mean()  # Excluding label 0 (background)
        std_size = sizes[1:].std()  # Standard deviation of sizes
        
        # Defining size boundaries for filtering: within one standard deviation of the mean size
        lower_bound = mean_size - std_size
        upper_bound = mean_size + std_size

        # Filtering labels based on size boundaries 
        filtered_labels = numpy.array([i for i, size in enumerate(sizes)
                                       if lower_bound <= size <= upper_bound])

        # Creating a mask that includes only the filtered labels
        filtered_mask = numpy.isin(label_array, filtered_labels)

        # Visualizing the filtered mask 
        plt.imshow(filtered_mask, cmap="gray")  # Display the filtered mask in grayscale
        plt.title(f"Filtered Mask: {gene}, {field}")  
        plt.show()  


### EXERCISE 3: SCORE THE PCNA AND NASCENT RNA SIGNAL IN EACH NUCLEUS AND PLOT THEM 

# Creating a placeholder dictionary to store results for each nucleus -> this will be the data table setup 
data = {
    "Gene": [],  # Gene name
    "nascentRNA": [],  # Mean nascent RNA signal for each nucleus
    "PCNA": [],  # Mean PCNA signal for each nucleus
    "ratio": []  # Log2 ratio of nascentRNA to PCNA signal for each nucleus
}

# Iterating through each gene and field in imgArray using for loop format 
for gene, fields in imgArray.items():
    for field_index, field_array in enumerate(fields):
        # Grabbing the corresponding label array and binary mask for the current gene and field
        label_array = label_maps[gene][field_index]  
        num_labels = numpy.amax(label_array) + 1  # Find the maximum label (total number of labeled nuclei, including background)

        # Skipping label 0 (background) and compute mean signals for each nucleus
        for label in range(1, num_labels):  # Excluding background by starting from 1 
            where = numpy.where(label_array == label)  # Getting pixel positions of the current nucleus

            # Calculating the mean signal for PCNA (channel 2)
            mean_pcna = numpy.mean(field_array[where[0], where[1], 2])  # PCNA is assumed to be in channel 2
            # Calculating the mean signal for nascent RNA (channel 1)
            mean_nascent_rna = numpy.mean(field_array[where[0], where[1], 1])  # Nascent RNA is assumed to be in channel 1

            # Calculating the log2 ratio of nascent RNA to PCNA signal, handle case where PCNA is 0 to avoid division by zero
            ratio = numpy.log2(mean_nascent_rna / mean_pcna) if mean_pcna > 0 else None

            # Appending the computed data above for this nucleus to the empty data dictionary
            data["Gene"].append(gene)
            data["nascentRNA"].append(mean_nascent_rna)
            data["PCNA"].append(mean_pcna)
            data["ratio"].append(ratio)

# Writing the data to a CSV text file by defining the output file name as 'gene_signal_data.txt' 
output_file = "gene_signal_data.txt"  
with open(output_file, "w", newline="") as file:
    # Initializing CSV writer with values separated by commas 
    writer = csv.writer(file, delimiter=",")  
    # Writing the header row same as the data dictionary created 
    writer.writerow(["Gene", "nascentRNA", "PCNA", "ratio"]) 
    # Iterating through each nucleus data
    for i in range(len(data["Gene"])):  
        writer.writerow([
            data["Gene"][i],
            data["nascentRNA"][i],
            data["PCNA"][i],
            data["ratio"][i]
        ])

# Printing confirmation after saving the data to double check it worked 
print(f"Data saved to {output_file}")

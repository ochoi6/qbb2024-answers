#!/usr/bin/env python

### Description: 

    # 24 single-channel images 
    # 4 different samples that each have 2 separate fields 
    # each sample-field has 3 channel images (DAPI, Alexa568, EU-Alexa488)


### EXERCISE 1: LOADING THE IMAGE DATA 

# Directions: create a for loop that...
    # Load the channel images into python with imageio.v3.imread function
    # Loop through list of gene names 
    # For each gene/field -> put all of the channels into same array so that image is (X, Y, 3) -> (width, height, # channels)
    # Should result in 8 x 3-colored image arrays 


# Import all the necessary packages into the environment 

import numpy
import scipy
import matplotlib.pyplot as plt
import imageio
import plotly
import plotly.express as px


# Creating an empty list to store the images 
all_images = []


# Creating a gene list 
genes = ["APEX1", "PIM2", "POLR2B", "SRSF1"]
print(genes)

# Creating a fields list 
fields = ["field0", "field1"]
print(fields) 

# enumerate 

for gene in genes:
    for field in fields:
        # Initialize a 3-channel image array (616 x 520 pixels)
        imgArray = numpy.zeros((520, 616, 3), numpy.uint16)

        # create a list of channels 

        # Load each channel and store it in the array
        imgArray[:, :, 0] = imageio.v3.imread(f"{gene}_{field}_DAPI.tif").astype(numpy.uint16)
        imgArray[:, :, 1] = imageio.v3.imread(f"{gene}_{field}_nascentRNA.tif").astype(numpy.uint16)
        imgArray[:, :, 2] = imageio.v3.imread(f"{gene}_{field}_PCNA.tif").astype(numpy.uint16)

        # Append the image array to the list
        all_images.append(imgArray)

        print(imgArray)

        # Print for debugging purposes 
        print(f"Processed: {gene}, {field}")
        print(imgArray.shape)

# single image with 3 dimensions is technically the 3rd fixed and the last question is for 1 and 2 -> keeping track of what dimensions i am working at the moment 


# .shape -> getting the dimensions - (dim0 = height, dim1 = length) -> change that 

### EXERCISE 2: IDENTIFYING INDIVIDUAL CELLS 


# Directions: Using the segmentation function used in live-coding to identify cells and then filtering them to remove outliers 

## Step 2.1: For each image, create a binary mask from DAPI channel 

## Step 2.2: Find labels for each image based on the DAPI mask from step 2.1

## Step 2.3: Filter out labeled ooutliers based on size 

# bigger than or equal to the mean of the image 
mask = img >= 0.035
plt.imshow(mask, cmap='grayscale')
plt.show()

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

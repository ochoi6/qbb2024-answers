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

for gene in genes:

    # dimeensions of the image might change depending on the gene 
    trial = imageio.v3.imread(f"{gene}_field0_DAPI.tif")

    # shape method -> to grab the width and the height of an image and storing it into dimensions variable 
    dimensions = trial.shape
    imgArray[gene] = []
    for field in fields:

        # Initialize a 3-channel image array filled with zeros and the dimenbsions that we stored previously (width, height)
        imgArray[gene].append(numpy.zeros((dimensions[0], dimensions[1], 3), numpy.uint16))

        # use enumerate in this step -> function: for a given vector or list, it will return an element and index to iterate through it 
        # going through channels, DAPi in C and 0 in j 
        for j, channel in enumerate(channels): 

            # j contains the channel index 
            # single pass through these 3 loops, now we have 4 variables to create a complex array that we were intially talking about 
            # for each channel of each gene of every field, we increment [i]
            imgArray[gene][-1][:, :, j] = imageio.v3.imread(f"{gene}_{field}_{channel}.tif")

            print(imgArray)






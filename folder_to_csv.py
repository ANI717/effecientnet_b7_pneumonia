#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Folder to CSV.

This script reads all files from a folder and creates three lists for training,
validation and testing. 

Revision History:
        2020-07-12 (Animesh): Baseline Software.

Example:
        $ python folder_to_csv.py

"""


#___Import Modules:
import os
import random
import numpy as np
import pandas as pd


#___Global Variables:
DIR = "data/images/train/NORMAL"
ODIR = "data/lists/NORMAL/"
LABEL = 0
# DIR = "data/images/train/PNEUMONIA"
# ODIR = "data/lists/PNEUMONIA/"
# LABEL = 1
# DIR = "data/images/test/NORMAL"
# ODIR = "data/lists/NORMAL/"
# LABEL = 0
# DIR = "data/images/test/PNEUMONIA"
# ODIR = "data/lists/PNEUMONIA/"
# LABEL = 1

# RATIO = [0.95, 0.05, 0] # [train, val, test]
RATIO = [0, 0, 1] # [train, val, test]
SEED = 717
RANDOM = 1 # True = 1, False = 0


#___Main Method:
def main():
    """This is the Main Method.

    This method contains procedure to create CSV lists.

    """
    
    # list all files in folder
    content = os.listdir(DIR)
    
    # create image list with proper directory path
    image = []
    for im in content:
        image.append(DIR + "/" + im)
    
    # shuffle list randomly
    if RANDOM == 1:
        random.seed(SEED)
        random.shuffle(image)
    
    # create labels
    label = [LABEL]*len(image)
    data = np.transpose(np.reshape(image + label, (2, -1)))
    
    # create training, validation and testing set
    train = data[0:int(len(data)*RATIO[0]), :]
    val = data[int(len(data)*RATIO[0]):int(len(data)*(RATIO[0]+RATIO[1])), :]
    test = data[int(len(data)*(RATIO[0]+RATIO[1])):, :]
    
    # create output directory if required
    if not os.path.exists(ODIR):
        os.mkdir(ODIR)
    
    # write lists in CSV files
    pd.DataFrame(train, columns =['image',
                'label']).to_csv(os.path.join(ODIR,"train.csv"), index=False)
    pd.DataFrame(val, columns =['image', \
                'label']).to_csv(os.path.join(ODIR,"val.csv"), index=False)
    pd.DataFrame(test, columns =['image', \
                'label']).to_csv(os.path.join(ODIR,"test.csv"), index=False)
    
    return None


#___Driver Program:
if __name__ == "__main__":
    main()


#                                                                              
# end of file
"""ANI717"""
# This file holds practice code for PYTHON

import os  # required to manipulate 

def createFolder(directory):

    try:

        if not os.path.exists(directory):

            os.makedirs(directory)

    except OSError:

        print ('Error: Creating directory. ' +  directory)


createFolder('./data/')
# Creates a folder in the current directory called data

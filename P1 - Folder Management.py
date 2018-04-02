# This file holds practice code for PYTHON.

# The purpose of this code is to create a lot of directories. Say we get a list
# of a hundred names in a Word document, how can you create individual folders
# for all these people in a certain place?

# Solution: We use a "for loop". This is something in programming that does
# something over and over again. Example:

for i in [5, 4, 2, 8, -1, -2]:  # for each thing in the brackets...
    print(i)

# This code prints all the numbers in the brackets one by one. It does 'print(i)'
# over and over again.

# We can also write

for i in range(5):
    print(i)

# This is different because we use 'range(5)'. This creates a bracketed list...
# [0, 1, 2, 3, 4] of ascending numbers. It's useful for iterating.

import os  # required to manipulate 

def createFolder(directory):

    try:

        if not os.path.exists(directory):

            os.makedirs(directory)

    except OSError:

        print ('Error: Creating directory. ' +  directory)


createFolder('./data/')
# Creates a folder in the current directory called data

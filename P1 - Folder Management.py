# This file holds practice code for PYTHON.

# The purpose of this code is to create a lot of directories. Say we get a list
# of a hundred names in a Word document, how can you create individual folders
# for all these people in a certain place?

# Solution: We use a "for loop". This is something in programming that does
# something over and over again. Example:

print('First bunch')
for i in [5, 4, 2, 8, -1, -2]:  # for each thing in the brackets...
    print(i)

# This code prints all the numbers in the brackets one by one. It does 'print(i)'
# over and over again.

# We can also write

print('Second Bunch')
for i in range(5):
    print(i)

# This is different because we use 'range(5)'. This creates a bracketed list...
# [0, 1, 2, 3, 4] of ascending numbers. It's useful for iterating.

import os  # here, we import some code someone else wrote. Its called 'os' and
            # lets us do things to the computer files.

nameList = open('RandomNames.txt')

print('one name from the list')
#print(nameList.readline())
print('a second name from the list')
#print(nameList.readline())

# These two lines above print a name from the list. Can you print all the names
# in the file? Try it out. The names are all in 'RandomNames.txt' in the
# repository.

##########################################################################

# This is the code that I wrote (solution)

#for i in range(50):
#    name = nameList.readline()
#    print(name)
#    if name:
#        os.mkdir('Names/' + name.rstrip('\n'))

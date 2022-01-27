# In order to read the data stored in a text file, you must open it first. 
# Just like a book. You can’t read what is inside if you don’t open it first.
"""There are four modes for opening a file:
r	for only reading files
w	for only writing to files
a	for adding to an existing file
"""


file1 = open("Week 10/Part 7/notes.txt","r")
readFile1 = file1.read()

print(readFile1)
file1.close()


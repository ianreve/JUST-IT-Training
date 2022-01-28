# Regular expressions are patterns that help a user match character combinations 
# in text files and strings. You can use regular expressions to filter or find a
# specific pattern in the output of a  command or a document.
#  Import the re module:

import re
"""\w = any alpha numeric char(any digits/character) = A-Z. Returns a match if the string 
contains alphanumeric characters including underscores. 
For example, \w will match a, b, c, d, 1, 2, 3, etc."""

# findall function
'''' RegEx findall method searches a string from the beginning to the end of the string, and return all the sub-string 
that matches the given regular expression in a list and returns an empty list if no match is found. '''


sentence =" Take up o one idea, One oh oof Idea at oop a time"
seacrhResult =  re.findall('o\w\w',sentence)
print(seacrhResult)

# the search "\w+" to match more characters
seacrhResult =  re.findall(r'o\w+',sentence)
print(seacrhResult)

# * zero or more repetitions of the preceding RegEx  characters/digits after the specified start character
seacrhResult =  re.findall(r'o\w*',sentence)
print(seacrhResult)

#  The question mark "?" RegEx use to match zero or one repetition of 
# alpha numeric characters starting with letter o
seacrhResult =  re.findall(r'o\w?',sentence)
print(seacrhResult)


# Regular expressions are patterns that help a user match character combinations 
# in text files and strings. You can use regular expressions to filter or find a
# specific pattern in the output of a  command or a document.
#  Import the re module:

import re
"""\w = any alpha numeric char(any digits/character) = A-Z. Returns a match if the string 
contains alphanumeric characters including underscores. 
For example, \w will match a, b, c, d, 1, 2, 3, etc."""

# # text/string to search
# sentence =" Take up one idea, One oof Idea at oop a time"

# # find all substring within the given string above that start with the letter "o"
# # followed by any two characters 
# # variable = module/library method search 
# seacrhResult =  re.search('o\w\w',sentence)

# # the group method is a method on the result that comes bach which will give us the exact subsring
# print(seacrhResult.group())

sentence =" Take up one idea, One oof Idea at oop a time"
seacrhResult =  re.search('i\w\w\w',sentence)
print(seacrhResult.group())
import re

# Match
# The RegEx Match method used, takes a regular expression 
# and search for that pattern right at the beginning of the string

sentence ="Take up o one idea, One oh oof Idea at oop a time"
"""only invoke the group in your result if if the result which 
comes back matches the substring at the start"""

seacrhResult =  re.match(r'T\w\w',sentence)
print(seacrhResult)
# print(seacrhResult.group())


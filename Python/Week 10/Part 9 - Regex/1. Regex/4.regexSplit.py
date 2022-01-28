import re

# Match
# The RegEx Match method used, takes a regular expression 
# and search for that pattern right at the beginning of the string

# \d  = 0-9 , \D = non digit characters, \s =white space , \S = non white space,
# Matches the preceding character one or more times. 
# The working of the + character is similar to *, but the + 
# character omits the pattern if the character doesn't occur. 
# For example, abc+ will match abc, abcc, abccc, etc. but not ab
sentence ="Tak0e up o on4e idea, 1One oh oof Ide6a at oop a time"

"\d  = 0-9 "
seacrhResult =  re.split(r'\D',sentence)
print("\n",seacrhResult,"\n")
seacrhResult =  re.split(r'\s',sentence)
print(seacrhResult,"\n")
seacrhResult =  re.split(r'\S',sentence)
print(seacrhResult,"\n")
import re

sentence ="Tak0e up o 02-12-2021 on4e idea, 2-06-21 1One oh oof Ide6a at 2-06-2020 oop a time"

# The curly braces "{}" RegEx use to specify a minimum and maximum 
# number of occurrences of the preceding RegEX  {min, max}, {max}'''
# \d  = 0-9 , \D = non digit characters, \s =white space , \S = non white space,
seacrhResult =  re.findall(r'\d{1,2}-\d{1,2}-\d{2}',sentence)
print("\n",seacrhResult,"\n")

seacrhResult =  re.findall(r'\d{1,2}-\d{1,2}-\d{2}\D',sentence)
print("\n",seacrhResult,"\n")

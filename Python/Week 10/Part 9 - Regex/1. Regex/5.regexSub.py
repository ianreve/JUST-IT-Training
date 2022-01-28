import re

sentence ="Tak0e up o on4e idea, 1One oh oof Ide6a at oop a time"

"\d  = 0-9 "
seacrhResult =  re.sub(r'One','two',sentence)
print("\n",seacrhResult,"\n")

#exercise4 substitute any substring that starts with
# the letter o regardless of the number of characters 
# that follows after

seacrhResult =  re.sub(r'o\d*','two',sentence)
print("\n",seacrhResult,"\n")

seacrhResult =  re.sub(r'o\w*','two',sentence)
print("\n",seacrhResult,"\n")
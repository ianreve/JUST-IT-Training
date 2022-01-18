from curses.ascii import isupper
from xml.sax.saxutils import prepare_input_source


s1="I am a python programmer" #string 
s2='I am a python programmer with single quote' # string
s3="""I am a python programmer with single quote I am a python programmer with 
single quote I am a python programmer with single quote"""
s4="How are you "

# print characters as per index
print(s2[7])

# print length of string 
print(len(s1))

# slice the string 
# start :end indexes
print(s4[1:3])
# start : index
print(s4[3:])

# : end index 
print(s4[:10])
print(s4[:len(s4)])

# penultimate value
print(s4[5:-1])

s5 = 'It is a beautiful day'
print(len(s5))
# print specific character start:end:step
print(s5[:21:2])

s6 = '123456789'
print(s6[:9:2])

# find method to find/locate substring within a given string
print(s5.find('day'))

# use left/right strip
s6 = ' It is a beautiful day '
print(s6.lstrip()) #left
print(s6.rstrip()) #right
print(s6.strip()) #both

# count a charcater in a string
print(s6.count('a'))

# uppercase and lowercase
print(s6.upper())
print(s6.lower())

# uppercase the first letter
print(s6.title())

# replace string
print(s6.replace("day","weather"))
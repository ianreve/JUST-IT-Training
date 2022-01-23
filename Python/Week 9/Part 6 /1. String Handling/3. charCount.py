# find the number of occurence of a specific character  in a string 
name = input('Enter your name: ').lower()
letter = input('Enter a letter: ').lower()

print(name.count(letter))

# solutiion 2
def characterCount(char, s):
    count = 0
    for c in s:
        if c.lower() == char.lower():
            count += 1
    return count

print(characterCount("g", "Goggles"))


varString = "This is python"
count = 0
findChar = input("Enter a a letter t search for ")

for aLetter in varString:
    # print(aLetter)
    if aLetter == findChar:
        count = count + 1
print("found ", findChar , count, "times")
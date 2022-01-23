# chr(): takes a decimal and returns the ascii equivalent
# ord(): takes a character and returns the decimal equivalent

def alphabets():
    alphabetList = []
    for letters in range(0, 121):
        alphabetList.append(chr(letters))
    return alphabetList

print(alphabets())
    
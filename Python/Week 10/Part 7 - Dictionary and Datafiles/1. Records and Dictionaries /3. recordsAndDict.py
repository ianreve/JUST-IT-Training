# Python stores recors in a dictionary and a dictionary is a collection of records 
dict1 = {1:"Jonh"}
dict2 = {1:"John",4:"Joel", 2:"Lucy", "cName": "Python"}

# access via index 
# print("User details is ",dict2(0))


# access via key
# print("User details is ",dict2[1])
dkeys =dict2.keys()
for key in dkeys:
    print(key)

dVals = dict2.values()
for value in dVals:
    print(value)
    # print(dict2[value])

print(dict2[4])

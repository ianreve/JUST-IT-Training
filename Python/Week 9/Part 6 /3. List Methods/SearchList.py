list1 = ["Tom", "Peter", "Harry", "Jane", "Janet", "Ada", "Anna"]
name = "Anna"
nameFound = [ names for names in list1 if name in list1 and name == names]
print(nameFound)


"solution"

findName = "Ada"

for name in list1:
    if name == findName:
        print("Found", findName)
        break
    else:
         print("Not Found", findName)

#///////////////
for i in range(len(list1)):
    if list1[i] == name: 
        print(f'{name} is in the list')
        break
else: print(f'{name} is not in the list')

set1 = {12,23,"Amy", 56,89,45,"Amy","Jane",89,4,"Lucy"} 
print(type(set1))
print(set1)

set1.update([10,"James","Don",45.1,-12]) # random order
print(set1)


# fset - frozen set 
fset = frozenset(set1)
fset.update([10,"Jameson","Dion",405.1,-321])
print(set1)

# exercise  create a set of mix datatypes
# update the set with at least two more items
# freeze the set and update the frozen set

set2 = {123,456,"Josh", "Alfie", -12,}

print(set2)
set2.update([10,"James"])
fset = frozenset(set2)
fset.update([2,"Molly"])
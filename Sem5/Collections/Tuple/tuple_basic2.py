# Loop through tuple
values = (10,20,30,40,50)
for value in values:
    print(value)
    
# Verify if item exists in tuple
if 200 in values:
    print("Value exists in tuple")
else:
    print("Value does not exists in tuple")
    
# Print tuple length
print("Total elements in tuple are :",len(values))

# Add item to tuple
lst = list(values)
lst.append(60)
values = tuple(lst)
print(values)

# Delete the tuple
# del values
# print(values)

# Create tuple with single value
tpl = (30,)
print(type(tpl))
print(tpl)

# Join two tuples
tpl1 = (10,20,30)
tpl2 = (40,50,60)
tpl3 = tpl1 + tpl2
print(tpl3)

# Declare tuple using constructor
tpl = tuple((1,2,3))
print(tpl)

# Count - Returns the number of times a specified value occurs in a tuple
tpl = (10,20,30,10,20,10)
print(tpl.count(20))

# index - Searches the tuple for a specified value and returns the position of where it was found
tpl = (10,20,30,40,50,30)
print(tpl.index(50,3))
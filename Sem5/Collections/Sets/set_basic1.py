s1 = {10,20,30,10,"India","Jay Hind","India"}
print(type(s1))
print(s1)
# print(s1[2]) - Will raise error as set is unordered and unindexed.

# Loop through the Set Collection
for i in s1:
    print(i)
    
# Check whether item exists in the set collection or not.
if 200 in s1:
    print("Data exists in set")
else:
    print("Data does not exists in set")
    
# Add items to set collection
s1.add(400)
print(s1)

s1.update((500,600))
print(s1)

# Get length of object
print(len(s1))

s2 = {10,20,30,40,10,20,30}
print(len(s2))

# Remove item from set collection
s1.remove(10)
s1.remove(500)
s1.remove(600)
# s1.remove(10) - Will raise error if item to remove does not exists.
# s1.remove(700) - Will raise error if item to remove does not exists.
s1.discard(20)
s1.discard(2000)
print(s1)

# Use pop method to remove item
s3 = {1,10,20,30,40,50,60}
print(s3)
s3.pop()
print(s3)

# Clear method
s3 = {10,20}
print(s3)
s3.clear()
s3.update([50,60])
print(s3)

del s3
s3.append(70)
print (s3) # Will raise error as s3 does not exists.
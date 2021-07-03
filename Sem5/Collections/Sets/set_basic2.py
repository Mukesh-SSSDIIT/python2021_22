# add() - Adds an element to the set
s1 = {10,20,30}
s1.add(40)
print(s1)

# clear() - Removes all the elements from the set
s1.clear()
print(s1)

# copy() - Returns a copy of the set
s1 = {10,20,30}
s2 = s1.copy()
print(s2)

# difference() - Returns a set containing the difference between two or more sets
s1 = {10,20,30}
s2 = {30,40,50}
s3 = s2.difference(s1)
print(s3)

# difference_update() - Removes the items in this set that are also included in another, specified set
s1 = {10,20,30}
s2 = {30,40,50}
s1.difference_update(s2)
print(s1)

# discard() - Remove the specified item
s1 = {10,20,30,40,50}
s1.discard(40)
print(s1)

# intersectoin() - Returns a set, that is the intersection of two other sets
s1 = {10,20,30,40}
s2 = {30,40,50}
s3 = s1.intersection(s2)
print(s3)

# intersection_update() = Removes the items in this set that are not present in other, specified set(s)
s1 = {10,20,30}
s2 = {30,40,50}
s1.intersection_update(s2)
# s1 = s1.intersection(s2)
print(s1)

# isdisjoint() - Returns whether two sets have a intersection or not
s1 = {10,20,30}
s2 = {30,40,50}
rv = s1.isdisjoint(s2)
print(rv)

# issubset() - Returns whether another set contains this set or not
s1 = {40,50}
s2 = {30,40,50}
rv = s1.issubset(s2)
print(rv)


# issuperset() - Returns whether this set contains another set or not
s1 = {10,20,30,40,50}
s2 = {10,40,50}
rv = s1.issuperset(s2)
print(rv)

# symmetric_difference() - Returns a set with the symmetric differences of two sets
s1 = {10,20,30}
s2 = {30,40,50}
s3 = s1.symmetric_difference(s2)
print(s3)

# symmetric_difference_update() - inserts the symmetric differences from this set and another

s1 = {10,20,30}
s2 = {30,40,50}
# s1 = s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)
print(s1)


list1 = ["aaa","bbb","ccc"]
list2 = [111,222,333]

list3 = list1 + list2

print(list1)
print(list2)
print(list3)

# Another way to join to lists.
# for i in list2:
#     list1.append(i)
    
# print(list1)

# Use extend method

list1.extend(list2)
print(list1)

list4 = list([1,2,3,4])
print(list4)

list5 = [10,20,10,20,30,40,30]
# Returns the number of elements with the specified value
print(list5.count(30))

# Returns the index of the first element with the specified value
print(list5.index(20))

# Adds an element at the specified position
print(list5)
list5.insert(2,100)
print(list5)

list6 = [10,5,20,15,30]
list6.reverse()
print(list6)

list6.sort(reverse=True)
print(list6)

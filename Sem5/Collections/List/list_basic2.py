numbers = [10,20,30,40,50]
print(numbers)

numbers.append(60)
# numbers.append(30)
# numbers.append(30)
print(numbers)

# numbers.remove(30)
# if 300 in numbers:
#     numbers.remove(300)
#     print(numbers)
# else:
#     print("300 is not in list")

# remove the element on specific index. Default is last index
ans = numbers.pop(4)
# numbers.pop()
# numbers.pop()
print(ans)
print(numbers)

del numbers[0]
print(numbers)

# numbers.clear()

print(numbers)

# del numbers

# print(numbers)


numbers_copy = numbers.copy()
print(numbers_copy)

numbers_copy1 = list(numbers)
print(numbers_copy1)


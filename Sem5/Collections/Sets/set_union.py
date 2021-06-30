# Using union method
s1 = {10,20,30}
s2 = {20,30,40}

s3 = s1.union(s2)
print(s1)
print(s2)
print(s3)
del s1,s2,s3

# Using update method
print("---------------------------")
s1 = {10,20,30}
s2 = {20,30,40}

s1.update(s2)
print(s1)
print(s2)
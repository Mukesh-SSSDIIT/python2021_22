# Creating tuple
print("------------------------")
t1 = (10,20,30,40,50)
print(t1)
print(type(t1))
print("Using Positive Indexing:",t1[3])
print("Using Negative Indexing:",t1[-2])


# Creating tuple with single value.
print("------------------------")
t2 = (20,)
print(t2)
print(type(t2))

# Specifying Range
print("------------------------")
t3 = (10,20,30,40,50,60,70,80,90,100)
#t4 = t3[2:7]
# t4 = t3[5:]
# t4 = t3[:5]
# t4 = t3[-5:-1]
# t4 = t3[-1:-5]
# t4 = t3[-1:]
# t4 = t3[:-5]
# t4 = t3[4:-7]
# t4 = t3[4:-2]
t4 = t3[:-10]
print(t4)

# Changing tuple value is not possible
print("------------------------")
t5 = (10,20,30,40,50)
lst5 = list(t5)
lst5[2] = 300
t5 = tuple(lst5)
print(t5)
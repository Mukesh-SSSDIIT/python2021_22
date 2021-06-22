def my_function(a,b):
    if(type(a) is int and type(b) is int):
        ans = a + b
        return ans
    else:
        return 0

v1 = my_function(10,20)
v2 = my_function("India"," is Great")
v3 = my_function("India",5)

print(v1,v2,v3)
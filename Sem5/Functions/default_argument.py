def my_power(base,pow=2):
    ans = 1
    for i in range(pow):
        ans *= base
    return ans

a = my_power(5,3)
b = my_power(4)
print(a,b)
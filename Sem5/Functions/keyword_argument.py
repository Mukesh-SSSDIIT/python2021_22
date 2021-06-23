def my_power(base,pow):
    ans = 1
    for i in range(pow):
        ans *= base
    return ans

print(my_power(pow=3,base=2))
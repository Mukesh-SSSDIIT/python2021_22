def my_factorial(num):
    if(num == 1):
        return 1
    else:
        ans = num * my_factorial(num-1)
        return ans

a = my_factorial(5)
print(a)
n = input("Enter an number : ")
n = int(n)
if(n<0):
    raise Exception("Negative values not allowed")
print(n)
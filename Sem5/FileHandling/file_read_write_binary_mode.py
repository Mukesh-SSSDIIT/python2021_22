f_object = open("data.bin","wb")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)
f_object.write(arr)
f_object.close()

f_object = open("data.bin","rb")
arr = f_object.read()
for v in arr:
    print (v)
f_object.close()
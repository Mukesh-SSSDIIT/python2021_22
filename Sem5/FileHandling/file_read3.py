f_object = open("data.txt","r")
# print(f_object.readline())
# print(f_object.readline())
# print(f_object.readline())

for line in f_object:
    print(line)

f_object.close()
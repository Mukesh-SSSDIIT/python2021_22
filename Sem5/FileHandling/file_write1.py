f_object = open("data1.txt","w")
f_object.write("This is file contents\n")
f_object.write("This is line number 2\n")
f_object.close()

f_object = open("data1.txt")
print(f_object.read())
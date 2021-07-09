# Will raise error if file does not exists.

f_object = open("data_r_plus_mode.txt","r+")
print(f_object.read())
f_object.write("test")
f_object.close()
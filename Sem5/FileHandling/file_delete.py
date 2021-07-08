import os

if(os.path.exists("data3.txt")):
    os.remove("data3.txt")
    print("File deleted successfully")
else:
    print("File does not exists")
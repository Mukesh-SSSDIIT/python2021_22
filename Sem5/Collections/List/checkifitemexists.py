students = ["Raj","Rohit","Ramesh","Ranjeet"]

nm = input("Enter student name to search : ")

if nm in students:
    print("Search found")
else:
    print(nm, "is not in our list")
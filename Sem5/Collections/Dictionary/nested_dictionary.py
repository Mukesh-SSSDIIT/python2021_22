students = {
    "student1" : {
                    "Name":"Mr. A",
                    "Age" : 19
    },
    "student2" : {
                    "Name":"Mr. B",
                    "Age" : 20
    },
    "student3" : {
                    "Name":"Mr. C",
                    "Age" : 18
    },
    "student4" : {
                    "Name":"Mr. D",
                    "Age" : 19
    },
}

print(students)
print(students["student1"]["Age"])
print(students["student3"]["Name"])

print("Name\t\tAge")
print("---------------------")
for student in students:
    print(students[student]["Name"],end="")
    print("\t\t",end="")
    print(students[student]["Age"])
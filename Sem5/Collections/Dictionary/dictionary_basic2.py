student_data = {"Name":"Rajesh","Class":"BCA","Sem":5}

for key in student_data:
    print(key, "-", student_data[key])
    
for val in student_data.values():
    print(val)

for key,val in student_data.items():
    print(key, "-" ,val)
    
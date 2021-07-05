student_data = {
                    "Name":"Rajesh1",
                    "Class":"BCA",
                    "Sem":5,
                    "University":"BKNMU",
                    "City":"Junagadh",
                }

for key in student_data:
    print(key, "-", student_data[key])
    
for val in student_data.values():
    print(val)

for key,val in student_data.items():
    print(key, "-" ,val)
    
if "Class" in student_data:
    print("Class is the key")
else:
    print("Class is not the key")
    
if "Rajesh" in student_data.values():
    print("Rajesh is available value in dictionary")
else:
    print("Rajesh is not available value in dictionary")
    
print(len(student_data))

tpl = student_data.popitem()
print(tpl)
print(student_data)

del student_data["Class"]
print(student_data)

student_data.clear()
print(student_data)

del student_data
# print(student_data)

student_data = {
                    "Name":"Rajesh1",
                    "Class":"BCA",
                    "Sem":5,
                    "University":"BKNMU",
                    "City":"Junagadh",
                }
s1 = student_data.copy()
print(s1)

s2 = dict(student_data)
print(s2)

s3 = dict(brand="Ford",Model=1994)
print(s3)


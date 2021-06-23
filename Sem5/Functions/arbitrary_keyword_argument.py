def my_function(**student):
    # print(student["fname"])
    # print(student["lname"])
    # print(student["age"])
    # print(student["std"])
    # print(student["city"])
    # print(student)
    for d in student:
        print(d, " : " , student[d])

my_function(fname="Bharat",lname="Pathak",age=19,std="BCA",city="Junagadh",admissionyear = 2018)
str_1 = "    Jay Hind     "
str_upper = str_1.upper()
str_lower = str_1.lower()
str_strip = str_1.strip()

print(str_1)
print(str_upper)
print(str_lower)
print(str_strip)

str1 = "####INDIA IS GREAT####"
print(str1.strip("#"))

str2 = "Python is the best language, I love Python. Python is user friendly"
str_search_result = str2.replace("Python","C Sharp",2)
print(str_search_result)


str3 = "Sagar, Bhavdip, Hardik, Kaushik, Jay"
result = str3.split(",",maxsplit=2)
for n in result:
    print(n.strip())
    
str4 = "Java:C Sharp:C Language:Python"
result = str4.split(":")
print(result)

str5 = "India"
str6 = "Great"
str7 = str5 + " " + str6
print(str7)

age = 20
str8 = "Your age is " + str(age)
print(str8)
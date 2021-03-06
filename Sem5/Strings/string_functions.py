s1 = "heLLo friends. åº» gOOD MornINg hEllo."
s1_cap = s1.capitalize()
print(s1_cap)

s1_casefold = s1.casefold()
print(s1_casefold)

s1_center = s1.center(50,"-")
print(s1_center)

s1_count = s1.casefold().count('hello')
print(s1_count)

s1_encode = s1.encode(encoding="ascii",errors="backslashreplace")
print(s1_encode)

s1_endswith = s1.endswith(".")
print(s1_endswith)

s2 = "H\te\tl\tl\to"
s2_expandtabs = s2.expandtabs(tabsize=10)
print(s2)
print(s2_expandtabs)

s1_find = s1.find("friendsooo")
print(s1_find)

s1_index = s1.index("friend")
print(s1_index)

# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# The index() method is almost the same as the find() method, 
# the only difference is that the find() method returns -1 if the 
# value is not found.

print("Country@123".isalnum())
print("Country".isalpha())
print("12123.50".isdecimal())
print("1212350".isdigit())

# A string is considered a valid identifier if it only contains 
# alphanumeric letters (a-z) and (0-9), or underscores (_).
# A valid identifier cannot start with a number, or contain any spaces.
print("sagar01_5".isidentifier())
print('India'.islower())

print('INDIA'.isupper())
print("India".istitle())
print("    ".isspace())
print("123.0".isnumeric())
print("123\\bc".isprintable())

tpl = ("Sagar","Kaushik","Rutvik","Nikhil")
str_join = ", ".join(tpl)
print(str_join)

nm = "Jay".ljust(20,"-")
print(nm,"is my friend")

nm = "            Rajesh             "
print("Hello,",nm.lstrip(), "How are you?")
print("Hello,",nm.rstrip(), "How are you?")
print("Hello,",nm.strip(), "How are you?")

nm = "BHARAT IS MY FRIEND"
mytable = nm.maketrans("ABCD","@$^&")
print(nm.translate(mytable))

nm = "I can eat banana all the day"
print(nm.partition("banana"))

txt = "Mi casa, su casa. Hi casa"
x = txt.rfind("casa")
print(x)

txt = "banana"
x = txt.rjust(20,"-")
print(x, "is my favorite fruit.")

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

txt = "50"
x = txt.zfill(10)
print(x)
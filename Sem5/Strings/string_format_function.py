nm = "Jay"
age = 20
stud_class = "BCA"

s1 = "Hello {}, and your age is {:.2f}, you are studying in {}"
s2 = s1.format(nm,age,stud_class)
print(s2)

s1 = "you are studying in {2}. Hello {0}, your age is {1:.5f} and , Bye {0}. Enjoy your {2}"
s2 = s1.format(nm,age,stud_class)
print(s2)

s1 = "Hello {name}, your age is {stud_age}"
s2 = s1.format(name=nm,stud_age=age)
print(s2)
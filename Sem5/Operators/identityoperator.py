class test:
    a = 5
    b = 6

obj1 = test()
obj2 = test()
obj3 = obj1
   
if(obj1 is obj2):
    print("The type of obj1 and obj2 are equal")
else:
    print("The type of obj1 and obj2 are not equal")
    
if(obj1 is obj3):
    print("The type of obj1 and obj3 are equal")
else:
    print("The type of obj1 and obj3are not equal")
    
if(obj2 is obj3):
    print("The type of obj2 and obj3 are equal")
else:
    print("The type of obj2 and obj3 are not equal")


x = 5 
if (type(x) is int): 
    print("true") 
else: 
    print("false")
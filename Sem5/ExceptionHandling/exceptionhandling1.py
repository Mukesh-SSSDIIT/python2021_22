try:
    n = input("Enter number : ")
    n = int(n)
    sq = n*n
    r = "Square of {} is {}"
    print(r.format(n,sq))
except:
    print("Some error occured")
else:
    print("Program executed without error")
finally:
    print("End of program")
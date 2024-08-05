print("Getting all needed inputs (a1x+b1y=c1; a2x+b2y=c2)")
a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))
a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))

if a1/a2-b1/b2==0:
    if b1/b2-c1/c2==0:
         print("There is an infinite ammount of solutions of the system")
    else :
        print("There is no solution of the system")
else :
    print("There is one solution of the system")
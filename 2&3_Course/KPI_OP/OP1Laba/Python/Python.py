import math
# Getting all needed values
c = float(input("Enter the hypotenuse: "))
a = float(input("Enter the leg: "))
# Calculating the second leg
b =  math.sqrt(pow(c,2)-pow(a,2))
# Outputing the results
print("The second leg is", b)

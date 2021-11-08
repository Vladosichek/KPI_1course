import math
import os
def arctg(a,l):
    result=0
    z=1
    i=1
    while math.fabs(z)>=10**l:
        z=((-1)**(i-1))*(a**(2*i-1))/(2*i-1)
        result += z
        i +=1
    return result

x=float(input("Enter x (x>=0):"))
j=int(input("Enter accuracy (10^e):"))
q=-j
t=float
u=float
c=float
if x<0:
    print("Invalid x")
else:
    if x<=1:
        print("y=arctg(x)+arctg(2x)")
        t = arctg(x,j)
        print("arctg(x):", round(t,q))
        if x<=0.5:
            u=arctg(2*x,j)
            print("arctg(2x):", round(u,q))
            c=t+u
            print("y=", round(c,q))
        else:
            print("arctg(2x) can not be counted because taylor series for arctg(a) can be used if |a|<=1")
            print("Error")
    else:
        print("y=arctg(x)/arctg(x-5)")
        print("arctg(x) can not be counted because taylor series for arctg(a) can be used if |a|<=1")
        print("Error")
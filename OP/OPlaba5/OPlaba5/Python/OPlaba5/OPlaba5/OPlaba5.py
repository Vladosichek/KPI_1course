a=float(input("Enter the number: "))
n=2
max=0
min=0
i=2
if a<2:
    print("The nearest max: 2")
else:
    while max<=a:
        for i in range (2, n+1, 1):
            if n%i==0:
                max=i
                break
        n+=1
    n=int(a)
    while min!=i:
        for i in range (2, n+1, 1):
            if n%i==0:
                min=n
                break
        n-=1
    if max-a>a-min:
        print("The nearest min: ", min)
    else:
        print("The nearest max: ", max)
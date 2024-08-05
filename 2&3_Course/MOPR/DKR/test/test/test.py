import random

#parameters
x = -2.0          #x of initial point
y = 3.0          #y of initial point
eps = 0.0001     #epsilon
it = 0           #iterator
am_acts = 0      #amount of operations

#my function
def f(x, y):
    return (x * y - x ** 3 - 1) ** 2 + (x ** 2 * y ** 2 + 5 * x - 9) ** 2

#minimization
while(True):

    #random choise between Ox and Oy
    chois = random.choice(['x', 'y'])

    #case Ox
    if chois == 'x':

        #calculation of needed parameters
        a = -2.0
        b = 2.0
        d = eps / 2
        x1 = (a + b - d) / 2
        x2 = (a + b + d) / 2
        f1 = f(x1, y)
        f2 = f(x2, y)

        #method of "dikhotomia"
        while(True):
            if f1 >= f2:
                a = x1
            else:
                b = x2
            x1 = (a + b - d) / 2
            x2 = (a + b + d) / 2
            f1 = f(x1, y)
            f2 = f(x2, y)
            am_acts += 1
            if abs(b - a) < eps:
                break
        x = (a + b) / 2

    #case Oy
    else:

        #calculation of needed parameters
        a = -1.0
        b = 3.0
        d = eps / 2
        y1 = (a + b - d) / 2
        y2 = (a + b + d) / 2
        f1 = f(x, y1)
        f2 = f(x, y2)

        #method of "dikhotomia"
        while(True):
            if f1 >= f2:
                a = y1
            else:
                b = y2
            y1 = (a + b - d) / 2
            y2 = (a + b + d) / 2
            f1 = f(x, y1)
            f2 = f(x, y2)
            am_acts += 1
            if abs(b - a) < eps:
                break
        y = (a + b) / 2
    it += 1
    print("No: %5d; x: %10.6f; y: %10.6f; f(x, y): %11.6f" % (it, x, y, f(x, y)))

    #conditions of ending minimization
    if(f(x, y) < eps):
        break
    if(it >= 1000):
        break
print("Amount of operations: %6d" % (am_acts))


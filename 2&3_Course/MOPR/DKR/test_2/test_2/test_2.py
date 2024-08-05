#parameters
x = -2.0 #x of initial point
y = 3.0 #y of initial point
eps = 0.0001 #epsilon
it = 0 #iterator
t = (3.0 - 5 ** 0.5) / 2.0 #parameter of GRS

#my function
def f(x, y):
    return (x * y - x ** 3 - 1) ** 2 + (x ** 2 * y ** 2 + 5 * x - 9) ** 2

#x derivative of f(x, y)
def dx(x, y):
    return -34 * x * y ** 2 + 6 * x ** 5 - 8 * x ** 3 * y - 2 * y + 6 * x ** 2 + 4 * x ** 3 * y ** 4 + 50 * x + 30 * x ** 2 * y ** 2 - 90

#y derivative of f(x, y)
def dy(x, y):
    return -34 * x ** 2 * y - 2 * x ** 4 - 2 * x + 4 * x ** 4 * y ** 3 + 20 * x ** 3 * y

#minimization
while(True):

    #calculation of needed parameters
    xnew = x - 0.1 * dx(x, y)
    ynew = y - 0.1 * dy(x, y)
    cx = x + t * (xnew - x)
    cy = y + t * (ynew - y)
    bx = x + xnew - cx
    by = y + ynew - cy

    #golden ratio search
    while(True):
        if f(cx, cy) <= f(bx, by):
            xnew = bx
            ynew = by
            bx = cx
            by = cy
            cx = x + xnew - bx
            cy = y + ynew - by
        else:
            x = cx
            y = cy
            cx = bx
            cy = by
            bx = bx - t * (xnew - x)
            by = by - t * (ynew - y)
        if abs(xnew - x) < eps:
            if abs(ynew - y) < eps:
                break
    x = xnew
    y = ynew
    it += 1
    print("No: %5d; x: %10.6f; y: %10.6f; f(x, y): %11.6f" % (it, x, y, f(x, y)))

    #conditions of ending minimization
    if(f(x, y) < eps):
        break
    if(it >= 1000):
        break



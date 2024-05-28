def plug():
    x = -100 #start at -100
    while x < 100: # Go up to 100
        if 2*x + 5 == 13: # If it makes the equation true
            print("x =", x) # Print out the answer
        x += 1

plug() # run the plug function


def g(x):
    return 6*x**3 + 31*x**2 + 3*x - 10

def plug2():
    x = -100
    while x < 100:
        if g(x) == 0:
            print("x = ", x)
        x += 1
    print("done.")

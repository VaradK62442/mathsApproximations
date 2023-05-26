import matplotlib.pyplot as plt
from math import sqrt


'''
Theon of Smyrna method for approximating the square root of 2

set x_0 = y_0 = 1 and for n >= 0:
x_(n+1) = x_n + y_n
y_(n+1) = 2x_n + y_n

then, y_n/x_n approximately equals the square root of 2
'''


# function to approximate square root of 2
# using theon of smyrna approximation
def sqrt2approx(n):
    # running totals
    x, y = 1, 1
    values = {}

    # repeat from 1 to n
    for i in range(1, n+1):
        # calculate x and y terms
        # add ratio to values dictionary
        x_next = x + y
        y_next = 2 * x + y

        values[i] = y / x

        # reset variables
        x = x_next
        y = y_next

    return values


# function to plot results, and square root of 2
# also plot differences from approximated value to actual value
def plot(n):
    # create dictionary of approximated values
    approximations = sqrt2approx(n)
    differences = [abs(val - sqrt(2)) for val in approximations.values()]

    plt.figure(1)
    plt.suptitle("Approximations")
    # plot values
    plt.plot(approximations.keys(), approximations.values())
    # plot sqrt(2)
    plt.plot([0, n], [sqrt(2), sqrt(2)])

    plt.figure(2)
    plt.suptitle("Differences")
    # plot differences
    plt.plot(approximations.keys(), differences)

    print(f'''
    sqrt(2): {sqrt(2)}
    Final approximation: {approximations[n]}
    Final differences: {differences[-1]}
    ''')

    plt.show()


plot(22) # only requires 22 iterations to have difference of 0 
# this is compared to sqrt(2) up to only 16 decimal places
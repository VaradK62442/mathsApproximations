import matplotlib.pyplot as plt
from math import pi, sqrt


'''
Function to approximate pi

In theory, 
pi/(2sqrt(2)) = 1 + 1/3 - 1/5 - 1/7 + 1/9 + 1/11 - 1/13 - 1/15 + ...
               = sum from n = 0 to infinity of ((-1)^n(1/(4n+1) + 1/(4n+3)))
=>
pi = 2sqrt(2)(1 + 1/3 - 1/5 - 1/7 + 1/9 + 1/11 - 1/13 - 1/15 + ...)
'''


# function to approximate pi by using newton's sum method
def pi_approx(n):
    # running total
    approximation = 0
    values = {}

    # repeat from 1 to n
    for i in range(0, n+1):
        # apply summation mentioned above
        # alternating positive and negative values
        # multiply by 2sqrt(2)
        approximation += (-1)**i * ((1/(4*i+1)) + (1/(4*i+3))) * 2 * sqrt(2)
        values[i] = approximation

    return values


# function to plot results, and pi constant
# also plot differences from predicted value to pi
def plot(n):
    # create dict of pi approximated values
    approximations = pi_approx(n)
    differences = [abs(val - pi) for val in approximations.values()]

    plt.figure(1)
    plt.suptitle("Approximations")
    # plot values
    plt.plot(approximations.keys(), approximations.values())
    # plot pi constant
    plt.plot([0, n], [pi, pi])

    plt.figure(2)
    plt.suptitle("Differences")
    # plot differences
    plt.plot(approximations.keys(), differences)

    print(f'''
    Pi: {pi}
    Final approximation: {approximations[n]}
    Final difference: {differences[-1]}
    ''')

    plt.show()


plot(1_000_000)
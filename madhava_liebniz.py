import matplotlib.pyplot as plt
from math import pi


'''
Function to approximate pi

In theory,
pi/4 = 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...
=>
pi = 4(1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...) = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
'''


# function to approximate pi by using madhava-liebniz approximation
def pi_approx(n):
    # running total
    approximation = 0
    values = {}

    # repeat from 1 to n
    for i in range(1, n+1):
        # add alternating negative and positive values
        # multiplied by reciprocal of odd numbers
        # multipled by 4
        approximation += (-1)**(i+1) * (1 / (2*i-1)) * 4
        values[i] = approximation

    return values


# function to plot results, and pi constant
# also plot differences from predicted value to pi
def plot(n):
    # create dict of pi approximated values
    approximations = pi_approx(n)
    differences = [abs(val - pi) for val in approximations.values()]

    plt.figure(1)
    plt.suptitle("Approximation")
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
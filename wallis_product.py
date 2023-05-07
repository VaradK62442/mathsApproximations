import matplotlib.pyplot as plt
from math import pi


'''
Function to approximate pi

In theory, the Wallis product states that
pi/2 = (2/1 * 2/3) * (4/3 * 4/5) * (6/5 * 6/7) * ...
=>
pi = 2(2/1 * 2/3 * 4/3 * 4/5 * 6/5 * 6/7 * ...)
'''


# function to approximate pi using wallis product method
def pi_approx(n):
    # running total
    approximation = 1
    values = {}

    for i in range(1, n+1):
        # multiply by 2*i / (2*i - 1) and by 2*i / (2*i + 1)
        approximation *= (2*i / (2*i - 1))
        approximation *= (2*i / (2*i + 1))
        values[i] = approximation * 2

    return values


# function to plot results, and pi constant
# also plot differences from predicted value to pi
def plot(n):
    approximations = pi_approx(n)
    differences = [abs(val - pi) for val in approximations.values()]

    # plot values
    plt.plot(approximations.keys(), approximations.values())
    # plot pi constant
    plt.plot([0, n], [pi, pi])
    # plot differences
    plt.plot(approximations.keys(), differences)

    print(f'''
    Pi: {pi}
    Final approximation: {approximations[n]}
    Final difference: {differences[-1]}
    ''')

    plt.show()


plot(1_000_000)
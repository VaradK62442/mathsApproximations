import matplotlib.pyplot as plt
from math import pi, sqrt, floor
import random


'''
Function to approximate pi

Suppose we have a floor made of parallel strips of wood, 
each the same width, and we drop a needle onto the floor. 
What is the probability that the needle will lie across a line between two strips?

This probability P is:
P = (2 * l) / (pi * t)

Rearranging for pi:
pi = (2 * l) / (t * P)

Where:
P is the probability that a needle will lie across a line between two strips
l is the length of the needle
t is the width of the strips

If we drop n needles, and h of those needles are crossing lines,
the probability P is approximated to be h / n
This gives the formula:
pi = (2 * l * n) / (t * h)
'''


'''
Method:

Draw imaginary lines representing boundaries of strips at intervals 5 units apart. 
Therefore t = 5
Pick a random point on the canvas, pick another point that is 2.6 units away from it.
Therefore l = 2.6 
See if this line (the needle) crosses any boundary line.
Repeat
'''


# function to approximate pi using Buffon's needle method
def pi_approx(reps, x_bound, y_bound, t, l):
    n, h = 0, 0
    
    # list for storing results
    results = []

    for _ in range(reps):
        # pick random x and y coordinate
        x_1, y_1 = (random.uniform(0, x_bound), random.uniform(0, y_bound))

        # pick second random x and y coordinate
        # such that the distance between the first set of points and this one is
        # equal to l

        # first, we define a set of points which describe a circle of radius l
        # around the chosen points
        # this can be described by the equation
        # (x - x_1)^2 + (y - y_1)^2 = l^2
        # where x_1 and y_1 are the first set of points
        # we then choose a random number between x_1 - l and x_1 + l as our value for x_2
        # we can then substitute x_2 into the above equation to get a value for y_2
        # this way, we can ensure that the second set of points will be l units away from the first set
        x_2 = random.uniform(x_1 - l, x_1 + l)

        # to find y_2, we substitute x_2 into the equation (x - x_1)^2 + (y - y_1)^2 = l^2
        # rearranging for y, we get
        y_2 = sqrt(l**2 - (x_2 - x_1)**2) + y_1

        # now we check if the line defined by our two sets of points lies on a boundary
        # we can do this by checking if there is a multiple of t within the ranges of the x-coordinates of the line
        # we do this by dividing the x-coordinates by t, to get a lower and upper bound on the multiple of t
        # if there is an integer within that range, then the needle crosses a boundary line

        # for example, if the needle has x-coordinates 145 and 180, dividing those values by t we get 2.9 and 3.6
        # since there is an integer between those values, we can see that the needle crosses a line
        # we can check if there is an integer between two values by flooring them and comparing them
        lower_bound = x_1 / t
        upper_bound = x_2 / t

        if abs(floor(upper_bound) - floor(lower_bound)) == 1:
            # if the needle is on a boundary, increment h
            h += 1
            crosses_line = True
        else:
            crosses_line = False

        # increment n no matter what
        n += 1

        try:
            approximation = (2 * l * n) / (t * h)
        except ZeroDivisionError:
            approximation = None

        # DEBUG
        # find distance between points
        dist = sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

        results.append({
            'x_1': x_1,
            'y_1': y_1,
            'x_2': x_2,
            'y_2': y_2,
            'n': n,
            'h': h,
            'approximation': approximation,
            'probability': h / n,
            'cross': crosses_line,
            # DEBUG
            'dist': dist
        })

    return results


# function to plot both needle drops and estimation results
def plot(results, x_bound, y_bound, t, l):
    plt.figure(1)
    # plot boundary lines
    for i in range(x_bound):
        if i % t == 0:
            plt.plot((i, i), (0, y_bound), 'k-')

    # plot needles
    for needle in results:
        if needle["cross"]:
            plt.plot((needle['x_1'], needle['x_2']), (needle['y_1'], needle['y_2']), 'g')
        else:
            plt.plot((needle['x_1'], needle['x_2']), (needle['y_1'], needle['y_2']), 'r')

    # plot results
    plt.figure(2)
    plt.plot([needle['n'] for needle in results], [needle["approximation"] for needle in results])
    plt.plot((0, len(results)), (pi, pi))

    # DEBUG
    # plot distances
    plt.figure(3)
    plt.plot([needle['n'] for needle in results], [needle["dist"] for needle in results])
    plt.plot((0, len(results)), (l, l))

    plt.show()


# main function
def main():
    # canvas is from coordinate (0, 0) to (1_000_000, 1_000_000)
    x_bound, y_bound = 2_000, 2_000

    # boundary lines are vertical, every t units
    # if t = 5, boundary lines are placed at x coordinates 0, 5, 10, 15, etc.
    t = 5
    l = 2.6

    res = pi_approx(2_000, x_bound, y_bound, t, l)
    plot(res, x_bound, y_bound, t, l)


main()
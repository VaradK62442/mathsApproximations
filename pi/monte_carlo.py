import matplotlib.pyplot as plt
from math import pi, sqrt
import random


'''
Function to approximate pi

The area of a circle with radius 1 is pi
The area of a square with radius 1 is 1
Hence, the ratio of the two areas is pi

We can simulate one quadrant of a circle, and the square inscribed around it.
We pick random points, and keep track of how many are in the circle and outside it.
The ratio of these two values should estimate pi/4, since we only have one quadrant.
'''


def pi_approx(n):
    results = []
    
    # initialise counters
    inside, outside, total = 0, 0, 0

    for _ in range(n):
        # square has coordinates from (-1, -1) to (1, 1)
        # pick random point
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)

        # check if point is inside circle
        # we can do this by checking if the distance of the point from the origin is
        # more or less than 1
        dist = sqrt(x**2 + y**2)

        if abs(dist) > 1:
            # point is outside the circle
            outside += 1
            in_circle = False
        else:
            # point is inside the circle
            inside += 1
            in_circle = True

        total += 1

        try:
            approximation = (inside / total) * 4
        except ZeroDivisionError:
            approximation = 0

        results.append({
            'x': x,
            'y': y,
            'inside': inside,
            'outside': outside,
            'total': total,
            'approximation': approximation,
            'in_circle': in_circle,
        })

    return results


def plot(results):
    plt.figure(1)
    plt.suptitle("Points")
    # plot points
    for point in results:
        if point['in_circle']:
            c = 'g'
        else:
            c = 'r'
    
        plt.scatter(point['x'], point['y'], c=c, s=3)
            
    # plot results
    plt.figure(2)
    plt.suptitle("Approximations")
    plt.plot([point['total'] for point in results], [point["approximation"] for point in results])
    plt.plot((0, len(results)), (pi, pi))

    plt.show()


def main():
    res = pi_approx(1_000)

    print(f'''
    Final approximation: {res[-1]["approximation"]}
    Final difference: {abs(res[-1]["approximation"] - pi)}
    ''')

    plot(res)


main()
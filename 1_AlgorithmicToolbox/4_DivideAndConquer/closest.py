# In this problem, your goal is to find the closest pair of points among the given n points. 
# This is a basic primitive in computational geometry having applications in, 
# for example, graphics, computer vision, traffic-control systems.

# Task: Given n points on a plane, find the smallest distance 
# between a pair of two (different) points. 
# Recall that the distance between points (x1, y1) and (x2, y2) 
# is equal to ((x1 - x2)^2 + (y1 - y2)^2)^0.5
# Input Format: 
# |-- The first line contains the number n of points. 
# |-- Each of the following n lines defines a point (xi, yi).
# Constraints: 2 <= n <= 10^5; -10^9 <= xi, yi <= 10^9 are integers.
# Output Format: Output the minimum distance. 
# The absolute value of the difference between the answer of your program 
# and the optimal value should be at most 10^−3. 
# To ensure this, output your answer with at least four digits after the decimal point 
# (otherwise your answer, while being computed correctly, 
# can turn out to be wrong because of rounding issues).

#Uses python3
import sys
import math

def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def min_crossing(Cx, Cy):
    min_d = float("inf")
    n = len(Cx)
    sort_by_y = sorted(zip(Cx, Cy), key = lambda x : x[1])
    for i in range(0, n):
        for j in range(i + 1, min(i + 8, n)):
            # print(i, j)
            a = [Cx[i], Cy[i]]
            b = [Cx[j], Cy[j]]
            d = dist(a, b)
            if d < min_d:
                min_d = d
    return min_d

def minimum_distance(x, y):
    min_d = float("inf")
    zipped = list(zip(x, y))
    n = len(x)
    if n <= 3:
        for i in range(n):
            for j in range(i + 1, n):
                d = dist(zipped[i], zipped[j])
                if d < min_d:
                    min_d = d
                    # print("base:", min_d)
                    return min_d
    else:
        zipped = sorted(zipped, key = lambda x : x[0])
        sort_x = [x for x, y in zipped]
        sort_y = [y for x, y in zipped]
        mid = n // 2
        # print("mid", mid)
        Lx = sort_x[:mid]
        Ly = sort_y[:mid]
        Rx = sort_x[mid:]
        Ry = sort_y[mid:]
        L_min = minimum_distance(Lx, Ly)
        R_min = minimum_distance(Rx, Ry)
        min_d = min(L_min, R_min)
        # print("d:", min_d)

        if n % 2 == 0:
            mid_value = (sort_x[mid - 1] + sort_x[mid])/2
        else:
            mid_value = sort_x[mid]
        # print("mid_value", mid_value)
        C_idx = [index for index, value in enumerate(sort_x) if \
             value >= (mid_value - min_d) and value <= (mid_value + min_d)]
        Cx = []
        Cy = []
        for i in C_idx:
            Cx.append(sort_x[i])
            Cy.append(sort_y[i])
        # print("C:", Cx, Cy)
        C_min = min_crossing(Cx, Cy)
        if C_min < min_d:
            min_d = C_min

    return min_d



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

    # n = 11
    # x = [4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2]
    # y = [4, -2, -4, 3 , 3,  0, 1, -1, -1, 2,  4]
    # print("{0:.9f}".format(minimum_distance(x, y)))

# You are responsible for collecting signatures from all tenants of a certain building. 
# For each tenant, you know a period of time when he or she is at home. 
# You would like to collect all signatures by visiting the building 
# as few times as possible.

# The mathematical model for this problem is the following. 
# You are given a set of segments on a line 
# and your goal is to mark as few points on a line as possible 
# so that each segment contains at least one marked point.

# Task: Given a set of n segments {[a0,b0],[a1,b1],...,[an−1,bn−1]} 
#       with integer coordinates on a line, 
#       find the minimum number m of points 
#       such that each segment contains at least one point. 
#       That is, find a set of integers X of the minimum size 
#       such that for any segment [ai,bi] there is a point x is an element of X 
#       such that ai <= x <= bi
# Input Format: 
# |-- The first line of the input contains the number n of segments. 
# |-- Each of the following n lines contains two integers ai and bi 
#     (separated by a space) defining the coordinates of endpoints of the i-th segment.
# Constraints: 1 <= n <= 100, 0 <= ai <= bi <= 10^9 for all 0 <= i < n 
# Output Format: 
# |-- Output the minimum number m of points on the first line 
# |-- and the integer coordinates of m points (separated by spaces) on the second line. 
# You can output the points in any order. 
# If there are many such sets of points, you can output any set.
# (It is not difficult to see that there always exist a set of points of the minimum size 
# such that all the coordinates of the points are integers.)
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []

    # sort the segments by s.end
    segments.sort(key = lambda seg: seg[1])
    # print(segments)

    i = 0
    while i < len(segments):
        current_point = segments[i].end
        points.append(current_point)
        while i < len(segments) \
            and segments[i].start <= current_point \
            and segments[i].end >= current_point:
            i+=1
        # print("!", points, "where i =", i)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
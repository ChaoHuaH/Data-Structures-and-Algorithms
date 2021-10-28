# You are going to travel to another city that is located d miles away from your home city. 
# Your can can travel at most m miles on a full tank 
# and you start with a full tank. 
# Along your way, there are gas stations at distances 
# stop1, stop2, . . . , stopn from your home city. 
# What is the minimum number of refills needed?

# Input Format: 
# |-- The first line contains an integer d. 
# |-- The second line contains an integer m. 
# |-- The third line specifies an integer n.
# |-- Finally, the last line contains integers stop1, stop2, . . . , stopn
# Input Format: Assuming that the distance between the cities is d miles, a car can travel at most m miles on a full tank, and there are gas stations at distances stop1 , stop2 , . . . , stopn along the way, output the minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to reach the destination, output −1.
# Constraints: 1 <= d <= 10^5, 1 <= m <= 400, 1 <= n <= 300, 
#              0 < stop1 < stop2 < ... < stopn < m
import sys

def compute_min_refills(distance, tank, n, stops):
    stops.insert(0, 0) # add first element as stop 0
    stops.append(distance) # add last element as destination
    # print(stops)
    numRefills = 0
    currentRefil = 0
    
    while currentRefil <= n:
        lastRefill = currentRefil
        while currentRefil <= n and \
            (stops[currentRefil + 1] - stops[lastRefill]) <= tank:
            currentRefil += 1
        
        if currentRefil == lastRefill:
            return -1
        
        if currentRefil <= n:
            numRefills += 1
    
    return numRefills


if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, n, stops))

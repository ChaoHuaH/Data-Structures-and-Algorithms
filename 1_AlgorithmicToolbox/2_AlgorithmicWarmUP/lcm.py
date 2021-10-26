# The least common multiple of two positive integers a and b 
# is the least positive integer m 
# that is divisible by both a and b
# Task: Given two integers a and b, find their least common multiple.
# Input: The two integers a and b are given in the same line separated by space
# Constraints: 1<= a,b <= 2*(10^9).
# Output Format: Output the least common multiple of a and b.

import sys
import random

def gcd(a, b):
    if a == 0 or b == 0:
        return 1
    while b != 0:
        temp = a % b
        a = b
        b = temp
    
    return a

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm(a, b):
    # find the greatest common divisor of a and b
    gcd_ab = gcd(a, b)

    return a * b // gcd_ab


if __name__ == "__main__":
    # while True:
    #     a, b = random.sample(range(2 * pow(10, 2)),2)
    #     print("a:", a)
    #     print("b:", b)
    #     naive = lcm_naive(a, b)
    #     efficient = lcm(a, b)
    #     if naive != efficient:
    #         print("Wrong:", naive, efficient);
    #         break
    #     else: 
    #         print("OK:", naive, efficient)

    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(a, b))

# Given two integers a and b, find their greatest common divisor
# Input: two integers a, b are given in the same line separated by space
# Constraints: 1 <= a, b <= 2*10^9
# Output: gcd(a, b)
import sys
# import random

# Naive Algorithm
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b)+1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

# Efficient Algorithm
# a1 = remainer when a is divided by b
# gcd(a, b) = gcd(a1, b)
# proof: 
# a = a1 + bq for some q
# d is divides a and b if and only if it divides a1 and b
def gcd(a, b):
    if a == 0 or b == 0:
        return 1
    while b != 0:
        temp = a % b
        a = b
        b = temp
    
    return a
    

if __name__ == "__main__":
    # while True:
    #     a, b = random.sample(range(2 * pow(10, 2)), 2)
    #     print("a:", a)
    #     print("b:", b)
    #     naive = gcd_naive(a, b)
    #     efficient = gcd(a, b)
    #     if naive != efficient:
    #         print("Wrong:", naive, efficient)
    #         break
    #     else:
    #         print("OK:", naive, efficient)

    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(gcd(a, b))
    

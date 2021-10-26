# In this problem, your goal is to compute Fn modulo m, 
# where n may be really huge: up to 10^18 
# Task: Given two integers n and m, 
# Output: Fn mod m (that is, the remainder of Fn when divided by m). 
# Input Format: two integers n and m given on the same line (separated by a space). 
# Constraints: 1<= n <= 10^18, 2 <= m <= 10^3
import sys
import random

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    remainder_n = [0, 1]
    previous = 0
    current = 1

    for _ in range(n):
        previous, current = current % m, (previous + current) % m
        # print(remainder_n)
        # print(previous, current)
        if previous == 0 and current == 1:
            break
        remainder_n.append(current)
    
    # remove the last value == 0
    remainder_n.pop(-1)
    # print(remainder_n)
    
    # calculate the length of the repeated period
    length = len(remainder_n)

    return remainder_n[n % length]


if __name__ == "__main__":
    # while True:
    #     n = random.randint(0, pow(10, 3))
    #     m = random.randint(1, pow(10, 3))
    #     print("n:", n)
    #     print("m:", m)
    #     naive = get_fibonacci_huge_naive(n, m)
    #     fast = get_fibonacci_huge(n, m)
    #     if naive != fast:
    #         print("Wrong:", naive, fast)
    #         break
    #     else:
    #         print("OK:", naive, fast)

    input = sys.stdin.readline()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))

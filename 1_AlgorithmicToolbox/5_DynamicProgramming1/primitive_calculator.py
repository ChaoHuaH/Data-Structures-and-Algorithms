# when n become bigger, Error occors:
# RecursionError: maximum recursion depth exceeded in comparison

# You are given a primitive calculator that can perform 
# the following three operations with the current number x: 
# multiply x by 2, multiply x by 3, or add 1 to x. 
# Your goal is given a positive integer n, 
# find the minimum number of operations needed to obtain the number n 
# starting from the number 1.

# Task: 
# Given an integer n, compute the minimum number of operations needed to 
# obtain the number n starting from the number 1.
# Input Format: The input consists of a single integer 1 <= n <= 10^6
# Output Format: 
# |-- In the first line, output the minimum number k of operations 
#     needed to get n from 1. 
# |-- In the second line output a sequence of intermediate numbers. 
#     That is, the second line should contain positive integers 
#     a0, a1,.., ak such that a0 = 1, ak = n and for all 0 <= i < k,
#     ai+1 is equal to either ai + 1, 2ai, or 3ai
#     If there are many such sequences, output any one of them.

# Uses python3
import sys

# Greedy Algorithm
def GreedyCalculator(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)
# n = 10
# sequence = list(GreedyCalculator(n))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')

def optimal_sequence_aux(n, k, s):
    if k[n - 1] >= 0:
        return (k[n - 1], s)

    # base case n = 1, 2, 3
    if n == 1:
        k[n - 1] = 0
        s[n - 1] = 1
    elif n == 2 or n == 3:
        k[n - 1] = 1
        s[n - 1] = 1
    # otherwise
    else:
        val1 = val2 = val3 = float("inf")
        val1 = optimal_sequence_aux(n - 1, k, s)[0]
        if n % 2 == 0:
            val2 = optimal_sequence_aux(n // 2, k, s)[0]
        if n % 3 == 0:
            val3 = optimal_sequence_aux(n // 3, k, s)[0]
        
        if val1 <= val2 and val1 <= val3:
            k[n - 1] = val1 + 1
            s[n - 1] = n - 1
        elif val2 <= val1 and val2 <= val3:
            k[n - 1] = val2 + 1
            s[n - 1] = n // 2
        else:
            k[n - 1] = val3 + 1
            s[n - 1] = n // 3

    return (k[n - 1], s)

def optimal_sequence(n):
    k = [-1 for i in range(n)]
    s = [ 1 for i in range(n)]
    val, s = optimal_sequence_aux(n, k, s)
    
    out = [n]
    while n > 1:
        out.append(s[n - 1])
        n = s[n - 1]
    
    return out


if __name__ == "__main__":
    # input = sys.stdin.read()
    # n = int(input)
    n = 96234
    # n = 10
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in reversed(sequence):
        print(x, end=' ')

# An inversion of a sequence a0, a1, ..., an-1 is a pair of indices 0 <= i < j < n such that ai > aj. 
# The number of inversions of a sequence in some sense measures 
# how close the sequence is to being sorted. 
# For example, a sorted (in non-descending order) sequence contains no inversions at all, 
# while in a sequence sorted in descending order any two elements constitute an inversion 
# (for a total of n(n - 1)/2 inversions) 

# Task: The goal in this problem is to count the number of inversions of a given sequence.
# Input Format: The first line contains an integer n, 
# the next one contains a sequence of integers a0, a1, ..., an-1
# Constraints: 1 <= n <= 10^5, 1 <= ai <= 10^9 for all 0 <= i < n
# Output Format: Output the number of inversions in the sequence.

# Uses python3
import sys

def merge(a, left, ave, right):
    number_of_inversions = 0
    n1 = ave - left + 1
    n2 = right - ave
    L = [0 for i in range(n1 + 1)]
    R = [0 for j in range(n2 + 1)]
    for i in range(n1):
        L[i] = a[left + i]
    L[-1] = float("inf")
    for j in range(n2):
        R[j] = a[ave + 1 + j]
    R[-1] = float("inf")
    # print(L, ":", R)

    i = 0
    j = 0
    k = left
    for k in range(left, right + 1):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
            number_of_inversions += (n1 - i)

    return number_of_inversions


def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right - left < 1:
        return number_of_inversions
    ave = (left + right) // 2
    # print(left, ave, right)
    number_of_inversions += get_number_of_inversions(a, left, ave)
    number_of_inversions += get_number_of_inversions(a, ave + 1, right)
    number_of_inversions += merge(a, left, ave, right)

    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, 0, len(a) - 1))

    # n = 5
    # a = [4, 2, 3, 9, 2, 9]
    # print(get_number_of_inversions(a, 0, len(a) - 1))

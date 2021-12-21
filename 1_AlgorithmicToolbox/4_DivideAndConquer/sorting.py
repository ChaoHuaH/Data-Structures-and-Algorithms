# The goal in this problem is to redesign a given implementation 
# of the randomized quick sort algorithm so that it works fast 
# even on sequences containing many equal elements.

# Task: To force the given implementation of the quick sort algorithm 
# to efficiently process sequences with few unique elements, 
# your goal is replace a 2-way partition with a 3-way partition. 
# That is, your new partition procedure should partition the array into three parts: 
# < x part, = x part, and > x part.
# Input Format: The first line of the input contains an integer n. 
# The next line contains a sequence of n integers a0, a1, ..., an-1
# Constraints: 1 <= 10^5; 1 <= ai <= 10^9 for all 0 <= i < n
# Output Format: Output this sequence sorted in non-decreasing order.

# Uses python3 
import sys
import random

def partition3(a, l, r):
    x = a[l]
    m1 = l
    m2 = l
    for i in range(l + 1, r + 1):
        if a[i] == x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]  
        elif a[i] < x:
            a[i], a[m1] = a[m1], a[i]
            m1 += 1
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
        # print(a)
    return m1, m2

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    
    # partition2
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1);
    # randomized_quick_sort(a, m + 1, r);

    # use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

    # n = 5
    # a = [2, 3, 9, 2, 2]
    # print(a)
    # print("=" * 30)
    # randomized_quick_sort(a, 0, n - 1)
    # for x in a:
    #     print(x, end=' ')

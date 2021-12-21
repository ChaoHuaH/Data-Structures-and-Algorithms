# In this problem, you will implement the binary search algorithm 
# that allows searching very efficiently (even huge) lists, 
# provided that the list is sorted

# Task: The goal in this code problem is to implement the binary search algorithm.
# Input Format:
# The first line of the input contains an integer n and a sequence a0 < a1 < ... < an-1 of n pairwise distinct positive integers in increasing order. 
# The next line contains an integer k and k positive integers b0, b1, ..., bk-1
# Constraints: 1 <= n, k <= 10^4 for all 0 <= i < n; 1 <= bj <= 10^9 for all 0 <= j < k
# OutputFormat: For all i from 0 to k -1,output an index 0 <= j <= n - 1 
# such that aj = bi or −1 if there is no such index.
import sys

def binary_search(keys, query):
    low = 0
    high = len(keys) - 1
    while low <= high:
        mid = (low + high) // 2
        # print(low, mid, high)
        if query == keys[mid]:
            return mid
        elif query > keys[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    # input = list()
    # for line in sys.stdin.readlines():
    #     input.append(map(int, line.split()))
    # num_keys, *input_keys = input[0]
    # num_queries, *input_queries = input[1]
    # num_keys = 5
    # input_keys = [1, 5, 8, 12, 15]
    # num_queries = 5
    # input_queries = [8, 1, 23, 1, 11]

    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')

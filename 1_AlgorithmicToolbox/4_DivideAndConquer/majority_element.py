# Majority rule is a decision rule that selects the alternative 
# which has a majority, that is, more than half the votes.
# Given a sequence of elements a1, a2, ..., an, 
# you would like to check whether it contains an element that 
# appears more than n/2 times.

# Task: The goal in this code problem is to check whether an input sequence contains a majority element. 
# Input Format: 
# |-- The first line contains an integer n
# |-- the next one contains a sequence of n non-negative integers a1, a2, ..., an
# Constraints: 1 <= n <= 10^5; 0 <= ai <= 10^9 for all 0 <= i < n
# Output Format: 
# Output 1 if the sequence contains an element that appears strictly more than n/2 times, and 0 otherwise.
import sys

def merge_major(left_array, right_array):
    if left_array[0][0] == right_array[0][0]:
        left_array[0].extend(right_array[0])
        left_array[1].extend(right_array[1])
        return left_array
    else:
        left_max = left_array[0][0]
        cnt = 0
        i = 0
        while i < len(right_array[1]):
            if right_array[1][i] == left_max:
                left_array[0].append(left_max)
                right_array[1].remove(left_max)
            else:
                i += 1
        right_max = right_array[0][0]
        cnt = 0
        i = 0
        while i < len(left_array[1]):
            if left_array[1][i] == right_max:
                right_array[0].append(right_max)
                left_array[1].remove(right_max)
            else:
                i += 1

        if len(left_array[0]) > len(right_array[0]):
            left_array[1].extend(right_array[0])
            left_array[1].extend(right_array[1])
            return left_array
        else:
            right_array[1].extend(left_array[0])
            right_array[1].extend(left_array[1])
            return right_array


def get_majority_element(a, left, right):
    mid = (left + right) // 2
    # print(left, mid, right)

    # base case
    if left == right:
        # print([[a[left]],[]])
        return [[a[left]],[]]
    # only two elements
    if left + 1 == right:
        if a[left] == a[right]:
            output = [[a[left], a[right]],[]]
        else:
            output = [[a[left]], [a[right]]]
        # print(output)
        return output
    
    # otherwise 
    left_array = get_majority_element(a, left, mid)
    right_array = get_majority_element(a, mid + 1, right)
    # print("left:", left_array)
    # print("right:", right_array)
    return merge_major(left_array, right_array)

if __name__ == '__main__':
    # n = 5
    # a = [2, 3, 9, 2, 2]
    # a = [1, 2, 3, 4, 4]
    # print(get_majority_element(a, 0, n - 1))

    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
        
    if len(get_majority_element(a, 0, n -1)[0]) > n // 2:
        print(1)
    else:
        print(0)
# Maximum Pairwise Product Problem
# Find the maximum product of two distinct numbers 
# in a sequence of non-negative integers.
# Input: A sequence of non-negative integers.
# Output: The maximum value that can be obtained 
#         by multiplying two different elements from the se- quence.
import random

def old(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pair_product(numbers):
    n = len(numbers)

    idx_first = -1
    for i in range(0, n):
        if (idx_first == -1) or (numbers[i] > numbers[idx_first]):
            idx_first = i

    idx_second = -1
    for j in range(0,n):
        if (j != idx_first) and ((idx_second == -1) or (numbers[j] > numbers[idx_second])):
            idx_second = j

    return (numbers[idx_first] * numbers[idx_second])


if __name__ == "__main__":
    # while True:
    #     input_n = random.randint(2, 5)
    #     input_numbers = []
    #     for i in range(0, input_n):
    #         input_numbers.append(random.randint(1, 10))
    #     print(input_numbers)
        
    #     old_pd = old(input_numbers)
    #     new_pd = max_pair_product(input_numbers)
    #     if old_pd != new_pd:
    #         print("Wrong anser: ", old_pd, new_pd)
    #         break
    #     else:
    #         print("OK: ", old_pd, new_pd)        
        
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pair_product(input_numbers))

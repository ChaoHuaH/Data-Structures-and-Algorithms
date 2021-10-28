# You are organizing a funny competition for children. 
# As a prize fund you have n candies. 
# You would like to use these candies for top k places in a competition 
# with a natural restriction that a higher place gets a larger number of candies. 
# To make as many children happy as possible, 
# you are going to find the largest value of k for which it is possible.

# Task: The goal of this problem is to represent a given positive integer n 
# as a sum of as many pairwise distinct positive integers as possible. 
# That is, to find the maximum k such that n 
# can be written as a1 + a2 + .. + ak 
# where a1, ..., ak are positive integers 
# and ai != aj for all 1 <= i < j <= k
# Input Format: The input consists of a single integer n.
# Constraints: 1 <= n <= 10^9 
# Output Format:
# |-- In the first line, output the maximum number k such that n can be represented as a sum of k pairwise distinct positive integers. 
# |-- In the second line, output k pairwise distinct positive integers that sum up to n (if there are many such representations, output any of them).
import sys

def optimal_summands(n):
    summands = [1]
    current_sum = 1
    current_price = 2

    while current_sum < n:
        if summands[-1] >= (n - current_sum):
            break
        summands.append(current_price)
        current_sum += current_price
        current_price += 1
        # print(current_sum)
    
    if current_sum < n:
        summands[-1] += (n-current_sum)

    return summands

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end = ' ')
    print('')



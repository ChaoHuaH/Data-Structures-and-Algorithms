# As we already know, a natural greedy strategy for the change problem 
# does not work correctly for any set of denominations. 
# For example, if the available denominations are 1, 3, and 4, 
# the greedy algorithm will change 6 cents using three coins (4 + 1 + 1) 
# while it can be changed using just two coins (3 + 3). 
# Your goal now is to apply dynamic programming for 
# solving the Money Change Problem for denominations 1, 3, and 4.

# Input Format: Integer money.
# Output Format: The minimum number of coins with denominations 1, 3, 4 that changes money. 
# Constraints: 1 <= money <= 10^3

# Uses python3
import sys

def get_change(m):
    change = [0 for i in range(m + 1)]
    change[1:5] = [1, 2, 1, 1]
    for j in range(5, m + 1):
        q = float("inf")
        for i in [1, 3, 4]:
            new_value = 1 + change[j - i]
            # print("m:", j, "i:", i, "new:", new_value)
            if new_value < q:
                q = new_value
        change[j] = q
        # print(change)
    return change[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

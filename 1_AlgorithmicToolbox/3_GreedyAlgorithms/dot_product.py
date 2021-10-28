# You have n ads to place on a popular Internet page. 
# For each ad, you know how much is the advertiser 
# willing to pay for one click on this ad. 
# You have set up n slots on your page and estimated 
# the expected number of clicks per day for each slot. 
# Now, your goal is to distribute the ads among the slots 
# to maximize the total revenue.

# Task: Given two sequences a1, a2, ..., an (ai is the profit per click of the i-th ad) and 
#       b1, b2, ..., bn (bi is the average number of clicks per day of the i-th slot), we need to partition them into n pairs (ai, bj) such that the sum of their products is maximized.
# Input Format: 
# |-- The first line contains an integer n
# |-- the second one contains a sequence of integers a1, a2, ..., an, the third one contains a sequence of integers b1, b2, ..., bn.
# Constraints: 1 <= n <= 10^3, -10^5 <= ai, bi <= 10^5 for all 1 <= i <= n
# Output Format: Output the maximum value of sum(aici), 
#                where c1, c2, . . . , c𝑛 is a permutation of b1,b2,...,b𝑛


import sys

def max_dot_product(a, b):   
    res = 0
    a.sort(reverse = True)
    b.sort(reverse = True)
    
    while a and a[0] > 0 and b[0] > 0:
        res += a[0] * b[0]
        a.pop(0)
        b.pop(0)
        # print(a)
        # print(b)
        # print(res)
        # print("------")
    
    # a and b are both < 0
    while a and a[-1] < 0 and b[-1] < 0:
        res += a[-1] * b[-1]
        a.pop(-1)
        b.pop(-1)
    
    # a[0] > 0 : bi <= 0
    while a and a[0] > 0:
        res += a[0] * b[0]
        a.pop(0)
        b.pop(0)
    
    # a[-1] < 0: b >= 0
    while a and a[-1] < 0:
        res += a[-1] * b[-1]
        a.pop(-1)
        b.pop(-1)

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    

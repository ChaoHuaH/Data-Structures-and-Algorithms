# You are given a set of bars of gold and your goal is to take as much gold as possible into your bag. 
# There is just one copy of each bar and for each bar you can either take it or not 
# (hence you cannot take a fraction of a bar).

# Task: Given n gold bars, find the maximum weight of gold that fits into a bag of capacity W.
# Input Format: 
#   The first line of the input contains the capacity W of a knapsack and the number n of bars of gold. 
#   The next line contains n integers w0, w1, ..., wn-1 defining the weights of the bars of gold. 
# Constraints: 1 <= W <= 10^4; 1 <= n <= 300; 0 <= w0, ..., wn-1 <= 10^5
# Output Format: Output the maximum weight of gold that fits into a knapsack of capacity W.

# Uses python3
import sys

def optimal_weight(W, w):
    n = len(w)
    w.insert(0, 0)
    val = [[0 for j in range(W+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            val[i][j] = val[i-1][j]
            if w[i] <= j:
                temp = val[i-1][j - w[i]] + w[i]
                if temp > val[i][j]:
                    val[i][j] = temp
            # print(val)
    return val[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    # W = 10
    # w = [3, 1, 8]
    print(optimal_weight(W, w))

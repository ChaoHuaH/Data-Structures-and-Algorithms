# Compute the length of a longest common subsequence of two sequences.

# Task: Given two sequences A = (a1, a2, ..., an) and B = (b1, b2, ..., bm) 
#       find the length of their longest common subsequence, 
# Input Format: First line: n Second line: a1, a2, ..., an. 
#               Third line: m Fourth line: b1, b2, ..., bm. 
# Constraints: 1 <= n, m <= 100; -10^9 < ai, bi < 10^9
# Output Format: Output p

#Uses python3
import sys

def lcs2(a, b):
    m = len(a)
    n = len(b)
    c = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            elif c[i][j - 1] >= c[i - 1][j]:
                c[i][j] = c[i][j - 1]
            else:
                c[i][j] = c[i - 1][j] 
    # print(c)
    return c[m][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

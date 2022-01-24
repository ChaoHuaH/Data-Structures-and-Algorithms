# Compute the length of a longest common subsequence of three sequences.

# Task: Given three sequences A = (a1, a2, ..., an), B = (b1, b2, ..., bm), and C = (c1, c2, .., cl), 
#       find the length of their longest common subsequence
# Input Format: First line: n Second line: a1, a2, ..., an. 
#               Third line: m Fourth line: b1, b2, ..., bm.  
#               Fifth line: l Sixth line: c1, c2, ..., cl
# Constraints: 1 <= n, m, l <= 100; -10^9 < ai, bi, ci < 10^9
# Output Format: Output p

#Uses python3
import sys

def lcs3(a, b, c):
    n = len(a)
    m = len(b)
    l = len(c)
    d = [[[0 for k in range(l+1)] for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, l+1):
                if a[i-1] == b[j-1] == c[k-1]:
                    d[i][j][k] = d[i-1][j-1][k-1] + 1
                elif d[i-1][j][k] >= d[i][j-1][k] and d[i-1][j][k] >= d[i][j][k-1]:
                    d[i][j][k] = d[i-1][j][k]
                elif d[i][j-1][k] >= d[i-1][j][k] and d[i][j-1][k] >= d[i][j][k-1]:
                    d[i][j][k] = d[i][j-1][k]
                else:
                    d[i][j][k] = d[i][j][k-1]
    # print(d)
    return d[n][m][l]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
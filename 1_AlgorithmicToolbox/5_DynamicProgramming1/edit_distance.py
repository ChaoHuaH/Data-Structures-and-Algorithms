# The edit distance between two strings is the minimum number of operations 
# (insertions, deletions, and substitutions of symbols) 
# to transform one string into another. 
# It is a measure of similarity of two strings. 
# Edit distance has applications, 
# for example, in computational biology, natural language processing, and spell checking. 
# Your goal in this problem is to compute the edit distance between two strings.

# Task: The goal of this problem is to implement the algorithm for computing the edit distance between two strings.
# Input Format: Each of the two lines of the input contains a string consisting of lower case latin letters. 
# Constraints: The length of both strings is at least 1 and at most 100.
# Output Format: Output the edit distance between the given two strings.

# Uses python3
def edit_distance(s, t):
    m = len(s)
    n = len(t)
    c = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(m + 1):
        c[i][0] = i
    for j in range(n + 1):
        c[0][j] = j
    # print(c)
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            # print("j:", j, "i:", i)
            if s[i - 1] == t[j - 1]:
                d = c[i - 1][j - 1]
            else:
                d = c[i - 1][j - 1] + 1
            l = c[i][j - 1] + 1
            u = c[i - 1][j] + 1
            c[i][j] = min(d, l, u)
            # print(c)
    return c[m][n]

if __name__ == "__main__":
    # s = "ab"
    # t = "ab"
    # print(edit_distance(s, t))
    print(edit_distance(input(), input()))

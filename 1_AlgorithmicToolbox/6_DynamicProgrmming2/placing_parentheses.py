# In this problem, your goal is to add parentheses to a given arithmetic expression 
# to maximize its value.

# Task: Find the maximum value of an arithmetic expression 
# by specifying the order of applying its arithmetic operations using additional parentheses.
# Input Format: 
#   The only line of the input contains a string s of length 2n + 1 for some n, with symbols s0, s1, ...s2n. 
#   Each symbol at an even position of s is a digit (that is, an integer from 0 to 9) 
#   while each symbol at an odd position is one of three operations from {+,-,*}.
# Constraints: 1 <= n <= 14 (hence the string contains at most 29 symbols).
# Output Format: 
#   Output the maximum possible value of the given arithmetic expression 
#   among different orders of applying arithmetic operations.

# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(i, j, M, m, op):
    minimum = float("inf")
    maximum = -float("inf")
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])  
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)

    return (minimum, maximum)


def get_maximum_value(dataset):
    d = list(map(int, dataset[::2]))
    op = list(dataset[1::2])
    # print("d:", d)
    # print("op:", op)
    # print("=" * 30)
    
    n = len(d)
    M = [[-float("inf") for i in range(n)] for j in range(n)]
    m = [[float("inf") for i in range(n)] for j in range(n)]

    # diagonal
    for i in range(n):
        m[i][i] = d[i]
        M[i][i] = d[i]
    
    # above i = j
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, M, m, op)
        # print(M)
        # print(m)
        # print("=" * 30)

    return M[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
    # st = "5-8+7*4-8+9"
    # print(get_maximum_value(st))

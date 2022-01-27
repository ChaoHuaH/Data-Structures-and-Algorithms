# You and two of your friends have just returned back home after visiting various countries. Now you would like to evenly split all the souvenirs that all three of you bought.

# Input Format: 
#   The first line contains an integer n. 
#   The second line contains integers v1, v2, ..., vn separated by spaces.
# Constraints: 1 <= n <= 20, 1 <= vi <= 30 for all i
# Output Format: 
#   Output 1, if it possible to partition v1, v2, ..., vn into three subsets with equal sums, 
#   and 0 otherwise.

# Uses python3
import sys
import itertools

def partition3(A):
    # naive: Theta(3^n)
    # for c in itertools.product(range(3), repeat=len(A)):
    #     sums = [None] * 3
    #     for i in range(3):
    #         sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

    #     if sums[0] == sums[1] and sums[1] == sums[2]:
    #         return 1

    s = sum(A)
    if s % 3 != 0:
        return 0
    avg = s // 3
    n = len(A)
    A.insert(0, 0) # index 0 
    # divide A into 3 groups
    # sum of each group of numbers = avg
    dp = [[[0 for j in range(avg+1)] for i in range(avg+1)] for n in range(n+1)]
    dp[0][0][0] = 1 # a0 = {} and x = 0, y = 0
    # print(dp)
    for ni in range(1, n+1):          # n items in 
        # print("A:", A[ni])
        for i in range(avg+1):     # set1: to sum to avg
            for j in range(avg+1): # set2: to sum to avg
                if dp[ni-1][i][j] == 1:
                    dp[ni][i][j] = 1
                elif i >= A[ni] and dp[ni-1][i-A[ni]][j] == 1:
                    dp[ni][i][j] = 1
                elif j >= A[ni] and dp[ni-1][i][j-A[ni]] == 1:
                    dp[ni][i][j] = 1
                else:
                    dp[ni][i][j] = 0
        # print(dp)
    return dp[n][avg][avg]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    # A = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
    # A = [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]
    # A = [3, 3, 3, 3]
    # A = [1, 3, 3, 2]
    print(partition3(A))


# Given an integer n, find the nth Fibonacci number Fn 
# Input: integer n
# Constraints: 0 <= n <= 45
# Output: Fn
# Fibonacci sequence: 
# F0 = 0, F1 = 1, Fi = Fi−1 + Fi-2 for i >= 2

def cal_fib(n):
    f0 = 0
    f1 = 1
    # print("f0: ", f0, "f1: ", f1)
    if n <= 1:
        return n
    else:
        for i in range(2, n+1):
            temp = f0
            f0 = f1
            f1 +=temp            
            # print(i, " > f0: ", f0, "f1: ", f1)

    return f1

n = int(input())
print(cal_fib(n))

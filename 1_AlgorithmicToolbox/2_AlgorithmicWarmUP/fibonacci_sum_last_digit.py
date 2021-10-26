# Last Digit of the Sum of Fibonacci Numbers
# The goal in this problem is to find the last digit of a sum of the first n Fibonacci numbers.
# Task: Given an integer n, find the last digit of the sum F0+F1+...+Fn 
# Input Format: The input consists of a single integer n
# Constraints: 0 <= n <= 10^18
# Output Format: Output the last digit of F0+F1+...+Fn 
import sys

# find the patter of Fn mode 10
def fibonacci_10(n):
    if n <= 1:
        return n
    
    previous = 0
    current = 1
    remainder_n = [0, 1]
    
    for _ in range(n-1):
        previous, current = current % 10, (previous + current) % 10
        if previous == 0 and current == 1:
            break
        remainder_n.append(current)
    remainder_n.pop(-1)

    return remainder_n

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10


def fibonacci_sum(n, list_fib10):
    if n <= 1:
        return n
    
    n_fib10 = len(list_fib10)
    if n > n_fib10:
        return  (sum(list_fib10) * (n // n_fib10) + sum(list_fib10[0: (n % n_fib10 + 1)])) % 10
    else:
        return sum(list_fib10[0: (n % n_fib10 + 1)]) % 10
    

if __name__ == "__main__":
    input = sys.stdin.readline()
    n = int(input)
    list_fib10 = fibonacci_10(100)
    print(fibonacci_sum(n, list_fib10))

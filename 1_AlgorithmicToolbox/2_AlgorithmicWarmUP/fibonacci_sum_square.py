# Last Digit of the Sum of Squares of Fibonacci Numbers
# Task: Compute the last digit of F0^2 + F1^2 + ... + Fn^2
# Input Format: integer n
# Constraints: 0 <= n <= 10^18
# Output Format: The last digit of F0^2 + F1^2 + ... + Fn^2

# the sum F1^2 + F1^2 + ... + F5^2 as the area of a rectangle 
# with vertical side F5 = 5 and horizontal side F5 + F4 = 3 + 5 = F6
import sys

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

# method 1
# def get_fibonacci_last_digit(n):
#     if n <= 1:
#         return n;
    
#     f0 = 0
#     f1 = 1
#     for _ in range(n - 1):
#         f0, f1 = f1 % 10, (f0 + f1) % 10

#     return f1

# def fibonacci_sum_squares(n):
#     if n <= 1:
#         return n
    
#     return get_fibonacci_last_digit(n) * get_fibonacci_last_digit(n+1) % 10

# method 2
# def fibonacci_sum_squares(n):
#     if n <= 1:
#         return n;
    
#     f0 = 0
#     f1 = 1
#     for _ in range(n):
#         f0, f1 = f1 % 10, (f0 + f1) % 10

#     return (f0 * f1) % 10

# method 3
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

def fibonacci_sum_squares(n, list_fib10):
    if n <= 1:
        return n
    
    n_fib10 = len(list_fib10)
    fn = list_fib10[n % n_fib10]
    fn1 = list_fib10[(n+1) % n_fib10]

    return (fn * fn1) % 10




if __name__ == "__main__":
    input = sys.stdin.readline()
    n = int(input)
    list_fib10 = fibonacci_10(100)
    print(fibonacci_sum_squares(n, list_fib10))
# find the last digit of a partial sum of Fibonacci numbers: 
# Fm + Fm+1 + ... + Fn
# Input: two non-negative integers m and n separated by a space
# Constraints: 0 <= m <= n <= 10^18
# Output: the last digit of Fm + Fm+1 + ... + Fn
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

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10

def fibonacci_sum(n, list_fib10):
    if n <= 1:
        return n
    
    n_fib10 = len(list_fib10)
    if n > n_fib10:
        return  (sum(list_fib10) * (n // n_fib10) + sum(list_fib10[0: (n % n_fib10 + 1)])) % 10
    else:
        return sum(list_fib10[0: (n % n_fib10 + 1)]) % 10

def fibonacci_partial_sum(from_, to, list_fib10):
    if from_ == 0:
        Fm = 0
    else:
        Fm = fibonacci_sum(from_-1, list_fib10)
    if to == 0:
        Fn = 0
    else:     
        Fn = fibonacci_sum(to, list_fib10) 
    # print("Fn:", Fn)
    # print("Fm:", Fm)

    if Fn < Fm:
        return Fn-Fm + 10
    else:
        return Fn - Fm

if __name__ == "__main__":
    input = sys.stdin.readline()
    m, n = map(int, input.split())
    list_fib10 = fibonacci_10(100)
    print(fibonacci_partial_sum(m, n, list_fib10))

# Your goal in this problem is to find 
# the last digit of nth Fibonacci number
# Recall that Fibonacci numbers grow exponentially fast
# For example
# F200 = 280571172992510140037611932413038677189525
import sys
# import random

# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % 10

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    
    f0 = 0
    f1 = 1
    for _ in range(n - 1):
        f0, f1 = f1 % 10, (f0 + f1) % 10

    return f1

if __name__ == "__main__":
    # while True:
    #     n = random.randint(0, 10000)
    #     naive = get_fibonacci_last_digit_naive(n)
    #     fast = get_fibonacci_last_digit(n)
    #     if naive != fast:
    #         print("Wrong: ", naive, fast);
    #         break
    #     else:
    #         print("OK: ", naive, fast)

    n = int(sys.stdin.readline())
    print(get_fibonacci_last_digit(n))

    
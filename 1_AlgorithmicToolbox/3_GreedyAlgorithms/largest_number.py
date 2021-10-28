# As the last question of a successful interview, 
# your boss gives you a few pieces of paper with numbers on it 
# and asks you to compose a largest number from these numbers. 
# The resulting number is going to be your salary, 
# so you are very much interested in maximizing this number. 
# How can you do this?

# Task: Compose the largest number out of a set of integers.
# Input Format: 
# |-- The first line of the input contains an integer n. 
# |-- The second line contains integers a1, a2, ..., an
# Constraints: 1 <= n <= 100, 1 <= ai <= 10^3 for all 1 <= i <= n
# Output Format: Output the largest number 
# that can be composed out of a1, a2, ..., an
import sys

def IsGreaterOrEqual(digit, maxDigit):
    str_digit = int(digit + maxDigit)
    str_maxDig = int(maxDigit + digit)

    if str_maxDig >= str_digit:
        return False
    else:
        return True


def largest_number(a):
    res = ""

    while a:
        maxDig = '0'
        for x in a:
            if IsGreaterOrEqual(x, maxDig):
                maxDig = x
        res += maxDig
        a.remove(maxDig)

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))



